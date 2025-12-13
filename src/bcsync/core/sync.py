from datetime import datetime
from typing import Optional, Dict, Any, List, Generator
from sqlalchemy import func, text, insert, select, delete
from sqlalchemy.orm import Session
from bcsync.api.client import BusinessCentralClient
from bcsync.core.types import EntitySyncConfig


def get_sync_timestamp(db_session: Session, sync_config: EntitySyncConfig, company_id: str) -> Optional[datetime]:
    """Helper function that returns max last modified timestamp for a specific entity on a company,
    to use as filter on api calls.
    :param db_session:
    :param sync_config:
    :param company_id:
    :return:timestamp:datetime
    """
    core_table = sync_config.core_model
    timestamp = db_session.scalar(
        select(
            func.max(
                core_table.system_modified_at)
        ).where(
            core_table.company_id == company_id
        )
    )
    return timestamp


def delete_staging_records(db_session: Session, sync_config: EntitySyncConfig, company_id: str) -> None:
    """
    Helper function that deletes all records in staging table for a specific company.
    :param db_session:
    :param sync_config:
    :param company_id:
    :return:None
    """
    staging_table = sync_config.staging_model
    db_session.execute(
        delete(
            staging_table
        ).where(
            staging_table.company_id == company_id
        )
    )


def yield_records_batches(bc_client: BusinessCentralClient,
                                   sync_config: EntitySyncConfig, last_modified_at: datetime,
                                   batch_size: int = 10000) -> Generator[List[Dict[str, Any]], None, None]:
    endpoint = sync_config.endpoint
    validator = sync_config.validator_model
    batch = []
    for page in bc_client.iter_pages(endpoint=endpoint, last_modified_at=last_modified_at):
        for record in page:
            validated_record = validator.model_validate(record).model_dump()
            batch.append(validated_record)
            if len(batch) >= batch_size:
                yield batch
                batch = []
    if batch:
        yield batch


def bulk_insert_to_staging(db_session: Session, bc_client: BusinessCentralClient,
                      sync_config: EntitySyncConfig, last_modified_at: datetime, batch_size : int = 10000) -> int:
    staging_table = sync_config.staging_model
    total_records = 0
    for batch in yield_records_batches(bc_client, sync_config, last_modified_at, batch_size):
        db_session.execute(
            insert(staging_table), batch
        )
        db_session.commit()
        total_records += len(batch)
    return total_records


def execute_load_procedure(db_session: Session, sync_config: EntitySyncConfig) -> Dict[str, Any]:
    """
    Helper function that executes load stored procedure for a specific entity.
    :param db_session:
    :param sync_config:
    :return:dict[Any, Any]
    """
    loader_procedure = sync_config.loader_procedure
    result = db_session.execute(text(f"EXEC {loader_procedure}")).mappings().first()
    return dict(result) if result else {}


def execute_fix_procedure(db_session: Session, sync_config: EntitySyncConfig) -> Dict[str, Any]:
    """
    Helper function that executes fixer stored procedure for a specific entity.
    :param db_session:
    :param sync_config:
    :return:dict[Any, Any]
    """
    fixer_procedure = sync_config.fixer_procedure
    result = db_session.execute(text(f"EXEC {fixer_procedure}")).mappings().first()
    return dict(result) if result else {}
