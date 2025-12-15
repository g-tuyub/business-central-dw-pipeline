import logging
from sqlalchemy import text, event, Connection
from bcsync.db.schemas import DBSchemas

logger = logging.getLogger(__name__)

#removes fk constraints checks on all tables
def disable_fks_listener(target, connection: Connection, **kw):
    """
        Event Listener ejecutado después de crear todas las tablas.
        Ejecuta la sentencia `ALTER TABLE ... NOCHECK CONSTRAINT ALL` en todas las tablas de la capa Core (DW).

        Motivación:
        - Permitir la carga de 'Late Arriving Dimensions' en el DW.
        - Mejorar el rendimiento del bulk insert.
        - Mantener la metadata de relaciones visible para herramientas como Power BI.
        """
    for table in target.tables.values():
        try:

            if table.info.get('enforce_fk_constraints'):
                logger.info(f"skipping table {table.name} since it has no FK constraints defined.")
                continue
            table_name = f"[{table.schema or 'dbo'}].[{table.name}]"
            logger.info(f"Disabling foreign key constraints for table: {table_name}")
            connection.execute(
                text(
                f"ALTER TABLE {table_name} NOCHECK CONSTRAINT ALL"
                )
            )
            logger.info("Disabled constraints successfully.")
        except Exception as e:
            logger.error(f'Disabling foreign key constraints failed with error : {e}')
            raise e

def create_schemas_listener(target, connection : Connection, **kw):
    """
    Event Listener ejecutado antes de crear las tablas.

    Verifica si los esquemas existen en la BD, si no, los crea.
    """

    for schema in DBSchemas:
        logger.info(f"Attempting to create db schema : {schema.name}")
        schema_name = schema.value
        try:
            connection.execute(
                text(f"""IF NOT EXISTS (SELECT * FROM sys.schemas WHERE name = '{schema_name}')
                        BEGIN 
                            EXEC('CREATE SCHEMA {schema_name}')
                        END
                    """)
            )
            logger.info(f"{schema_name} created successfully.")
        except Exception as e:
            logger.error(f'Failed to create db schema : {schema_name}')
            raise e


def register_all_listeners(metadata):
    event.listen(metadata, 'before_create', create_schemas_listener)
    event.listen(metadata, 'after_create', disable_fks_listener)
