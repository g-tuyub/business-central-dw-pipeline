import time
from sqlalchemy.orm import Session
from sqlalchemy import insert, select, func, text
from bcsync.api.client import BusinessCentralClient
from bcsync.db.engine import get_engine
from bcsync.config.config import Config
import logging
from typing import List, Optional
from bcsync.core.base import BCEntity, EntitySyncConfig, SYNC_TARGETS
from sqlalchemy import Engine

logger = logging.getLogger(__name__)


def stage_entity(db_engine: Engine, api_client: BusinessCentralClient, sync_config: EntitySyncConfig) -> None:
    run_metrics = {
        "extraction_time": 0.0,
        "validation_time": 0.0,
        "insertion_time": 0.0,
        "total_rows_inserted": 0,
    }

    with Session(db_engine) as session:
        last_modified = session.scalar(
            select(func.max(sync_config.core_model.system_modified_at))
            .where(sync_config.core_model.company_id == api_client.company_id)
        )

        logger.info(f"performing TRUNCATE TABLE on : {sync_config.staging_table}")
        session.execute(text(f"TRUNCATE TABLE {sync_config.staging_schema}.{sync_config.staging_table};"))
        session.commit()

        all_records = []

        t_extraction_start = time.perf_counter()

        for page in api_client.iter_pages(endpoint=sync_config.endpoint, last_modified_at=last_modified):
            t_extraction_end = time.perf_counter()
            run_metrics["extraction_time"] += t_extraction_end - t_extraction_start

            t_validation_start = time.perf_counter()
            validated_page = [
                sync_config.validator_model.model_validate(r).model_dump()
                for r in page
            ]
            t_validation_end = time.perf_counter()
            run_metrics["validation_time"] += t_validation_end - t_validation_start

            all_records.extend(validated_page)
            run_metrics["total_rows_inserted"] += len(validated_page)

            if len(all_records) >= 5000:
                t_insertion_start = time.perf_counter()
                session.execute(insert(sync_config.staging_model), all_records)
                session.commit()
                all_records = []
                t_insertion_end = time.perf_counter()
                run_metrics["insertion_time"] += t_insertion_end - t_insertion_start

            t_extraction_start = time.perf_counter()

        if all_records:
            t_insertion_start = time.perf_counter()
            session.execute(insert(sync_config.staging_model), all_records)
            session.commit()

            run_metrics["insertion_time"] += (time.perf_counter() - t_insertion_start)

    total_time = run_metrics["extraction_time"] + run_metrics["validation_time"] + run_metrics["insertion_time"]

    logger.info(f"sync metrics details for table : {sync_config.staging_model.__tablename__}")
    logger.info(f"Total extraction time : {run_metrics['extraction_time']}")
    logger.info(f"Total validation time : {run_metrics['validation_time']}")
    logger.info(f"Total insertion time : {run_metrics['insertion_time']}")

    logger.info(
        f"A total of {run_metrics['total_rows_inserted']} rows were inserted to staging. Elapsed time: {total_time} seconds")


def load_entity_core(db_engine: Engine, sync_config: EntitySyncConfig) -> None:
    try:
        metrics = {"inserted": 0, "updated": 0, "fixed": False, "load_time": 0.0}
        t_start = time.perf_counter()
        with Session(db_engine) as session:}
            result = db_session.execute(f'EXEC {sync_config.loader_sp)
            row = result.fetchone()
            if row:
                metrics["inserted"] = getattr(row, 'rows_inserted', 0)
                metrics["updated"] = getattr(row, 'rows_updated', 0)
            if sync_config.fixer_sp:
                session.execute(text(f"EXEC {sync_config.fixer_sp}"))
                metrics["fixed"] = True
            session.commit()
    except Exception as e:
        session.rollback()
            logger.error(f"Unable to load from {sync_config.staging_schema} to {sync_config.core_schema} for table: {sync_config.core_table} due to an error : {e}")
            raise e
        
    
    


def run_sync(config : Optional[Config] = None, entities_to_sync: Optional[List[BCEntity]] = None):
    config = config or Config.from_env()
    engine = get_engine(config.db.connection_string)
    client = BusinessCentralClient(config=config.api)
    targets = []

    if entities_to_sync:
        for bc_entity in entities_to_sync:
            sync_config = SYNC_TARGETS.get(bc_entity)
            if sync_config:
                targets.append(sync_config)
    else:
        targets = list(SYNC_TARGETS.values())

    for sync_config in targets:
            sync_entity(db_engine=engine, api_client=client, sync_config=sync_config)

if __name__ == "__main__":
    run_sync()
