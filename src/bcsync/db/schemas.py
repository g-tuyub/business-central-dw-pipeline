from enum import StrEnum, auto


class DBSchemas(StrEnum):
    """
    Esquemas físicos del Data Warehouse, centralizados aquí.
    """
    STAGING = auto()
    CORE = auto()
    SEMANTIC = auto()