import logging
from typing import List, Optional
from bcsync.core.types import EntitySyncConfig, BCEntity
from bcsync.core.registry import SYNC_TARGETS
from bcsync.db.schemas import DBSchemas
from bcsync.db.models.base import Base

logger = logging.getLogger(__name__)

def get_sorted_configs(targets: List[EntitySyncConfig]) -> List[EntitySyncConfig]:
    targets_map = {
        c.core_table: c for c in targets
    }

    all_sorted_tables = Base.metadata.sorted_tables

    sorted_configs = []

    processed_tables = set()

    for table in all_sorted_tables:
        if table.schema == DBSchemas.CORE and table.name in targets_map:
            config = targets_map[table.name]
            sorted_configs.append(config)
            processed_tables.add(table.name)

    for c in targets:
        if c.core_table not in processed_tables:
            sorted_configs.append(c)

    return sorted_configs


def resolve_configs_execution_order(targets: Optional[List[BCEntity]]) -> List[EntitySyncConfig]:
    """
    Helper function that returns a topologically sorted list of synchronization targets, given a list of entities.
    If no list provided, returns sorted list of all synchronization targets registered in SYNC_TARGETS.
    :param targets: Optional[List[BCEntity]]
    :return: List[EntitySyncConfig]
    """
    targets_to_resolve = []
    if targets:
        for target in targets:
            config = SYNC_TARGETS.get(target)
            if config:
                targets_to_resolve.append(config)
            else:
                logger.warning(f'Target entity {target} not registered in SYNC_TARGETS.')
    else:
        targets_to_resolve = list(SYNC_TARGETS.values())
    return get_sorted_configs(targets_to_resolve)