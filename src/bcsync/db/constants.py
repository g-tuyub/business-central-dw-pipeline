from bcsync.db.schemas import DBSchemas

NULL_UUID = "00000000-0000-0000-0000-000000000000"
MIN_BC_DATETIME = "0001-01-01 00:00:00"
UNKNOWN_MEMBER_ID = -1
UNKNOWN_TEXT = '<UNKNOWN>'
NULL_DATE = '0001-01-01'


SQL_CONTEXT = {
    'staging_schema' : DBSchemas.STAGING,
    'core_schema' : DBSchemas.CORE,
    'semantic_schema' : DBSchemas.SEMANTIC,
    'unknown_id' : UNKNOWN_MEMBER_ID,
    'unknown_text' : UNKNOWN_TEXT,
    "null_uuid": NULL_UUID,
    "min_datetime": MIN_BC_DATETIME,
    "null_date": NULL_DATE,
}

NAMING_CONVENTION = {
    "ix": "ix_%(column_0_N_label)s",
    "uq": "uq_%(table_name)s_%(column_0_N_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_N_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}