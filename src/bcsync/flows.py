from typing import Dict, Any, Optional, List
from dotenv import load_dotenv
from prefect import task, flow, get_run_logger, unmapped
from prefect.futures import wait
from prefect.artifacts import create_table_artifact
from prefect.states import Completed, Failed
from bcsync.core.utils import resolve_configs_execution_order
from bcsync.config.config import Config
from bcsync.api.client import BusinessCentralClient
from bcsync.core.types import EntitySyncConfig, BCEntity, SyncMetrics
from bcsync.db.engine import get_engine
from sqlalchemy.orm import Session
from bcsync.core.sync import (
    execute_load_procedure,
    execute_fix_procedure,
    delete_staging_records,
    get_sync_timestamp,
    bulk_insert_to_staging
)


@task(task_run_name='fase-1-{sync_config.core_table}',tags=['bc-api-limit'])
def staging_task(config: Config, sync_config: EntitySyncConfig) -> int:
    logger = get_run_logger()
    logger.info('Inicializando proceso de Extracción y Carga : API Business Central -> Tabla Staging en DW.')
    engine = get_engine(config.db.connection_string)
    client = BusinessCentralClient(config.api)
    with Session(engine) as session:
        #clean staging table before retrieving new records:
        logger.info('Limpiando datos de staging...')
        delete_staging_records(session, sync_config, client.company_id)
        logger.info('Datos eliminados correctamente.')
        timestamp = get_sync_timestamp(session, sync_config, client.company_id)
        logger.info(f'última fecha de sincronización : {timestamp}')
        #retrieve and insert records modified since last sync:
        logger.info(f'Obteniendo datos modificados después de {timestamp} en API endpoint: {sync_config.endpoint}')
        staged_records = bulk_insert_to_staging(session, client, sync_config, timestamp)
        logger.info(f'Inserción masiva a Staging realizada con éxito. {staged_records} registros insertados')
        session.commit()
    return staged_records


@task(task_run_name='fase-2-{sync_config.core_table}')
def merge_task(config: Config, sync_config: EntitySyncConfig, staged_records: int) -> Dict[str, Any]:
    logger = get_run_logger()
    metrics = {
        'rows_inserted': 0,
        'rows_updated': 0,
        'rows_fixed': 0
    }
    if staged_records > 0:
        engine = get_engine(config.db.connection_string)
        with Session(engine) as session:
            # execute loader
            logger.info('Iniciando proceso de Transformación, Carga : Tabla Staging en DW -> Tabla Core en DW.')
            load_result = execute_load_procedure(session, sync_config)
            # if rows were loaded and a fixer exists for this entity, execute fixer:
            if load_result:
                metrics['rows_inserted'] = load_result.get("rows_inserted", 0)
                metrics['rows_updated'] = load_result.get("rows_updated", 0)
                logger.info(
                    f'proceso de transformación y carga finalizado correctamente. Se insertaron {metrics["rows_inserted"]} registros, y se actualizaron {metrics["rows_updated"]} registros.')
                if sync_config.fixer_procedure:
                    fix_result = execute_fix_procedure(session, sync_config)
                    metrics['rows_fixed'] = fix_result.get("rows_fixed", 0)
                    logger.info(
                        f'Proceso de resolución de referencias finalizado correctamente. Se repararon {metrics["rows_fixed"]} registros.')
            session.commit()
        return metrics
    return metrics


@flow(name='actualizar-tablas-datawarehouse-business-central',
      description='Flujo principal para sincronizar todas las tablas de Business Central en el datawarehouse de SQL Server, para una empresa específica.')
def sync_entities(config_block: Optional[str] = None, entities_to_sync: Optional[List[BCEntity]] = None):
    logger = get_run_logger()
    if config_block:
        config = Config.from_prefect_block(config_block)
    else:
        load_dotenv()
        config = Config()
    targets = resolve_configs_execution_order(entities_to_sync)
    logger.info(f'Iniciando flujo principal de sincronizacion para {len(targets)} tablas.')

    #run staging tasks concurrently (API call + BULK INSERT)
    staging_futures = staging_task.map(unmapped(config), targets)
    logger.info('Fase Staging iniciada.')
    wait(staging_futures)
    logger.info('Fase Staging finalizada.')
    run_metrics = []
    logger.info('Fase Transformación y Resolución de referencias iniciada.')
    for sync_config, future in zip(targets, staging_futures):
        metrics = SyncMetrics(
            table=sync_config.core_table,
            endpoint=sync_config.endpoint
        )
        #run stored procedures (LOADERS -> FIXERS) sequentially after staging phase is completed.
        load_future = merge_task.submit(config, sync_config, future)  # type: ignore

        try:
            load_metrics = load_future.result()
            if load_metrics:
                metrics.rows_extracted = future.result()
                metrics.rows_inserted = load_metrics.get("rows_inserted", 0)
                metrics.rows_updated = load_metrics.get("rows_updated", 0)
                metrics.rows_fixed = load_metrics.get("rows_fixed", 0)
                metrics.state = 'SUCCESS'

        except Exception as e:
            logger.error(
                f'no se obtuvieron metricas de resultado debido a que fallo la tarea. marcando como "Fallida" : {e}')
            metrics.state = 'FAILURE'
        run_metrics.append(metrics)
    create_table_artifact([m.model_dump() for m in run_metrics], 'reporte-ejecucion')
    failed_count = sum(1 for m in run_metrics if m.state == 'FAILURE')
    if failed_count > 0:
        return Failed(
            message=f'Flujo de sincronización concluido con {failed_count} tareas fallidas. Revisa los detalles de ejecución en el artifact correspondiente.',
            result=run_metrics)
    return Completed(
        message='Flujo de sincronización concluido de manera exitosa. Se actualizaron todas las entidades solicitadas. evisa los detalles de ejecución en el artifact correspondiente.',
        result=run_metrics)


if __name__ == '__main__':
    sync_entities(config_block='config-bc-mexico')
