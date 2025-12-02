"""
bcsync.db.models.base
~~~~~~~~~~~~~~~~~~~~~
En este módulo se definen las clases Base del ORM para el sistema de sincronización al Data Warehouse:
Se estandariza el comportamiento de cada esquema (staging, core) usando composición y herencia de clases.

Uso:

    >>> from bcsync.db.models.base import CoreBase, StagingBase
    # Definir una tabla en la capa Core (Data Warehouse):
    class Customer(CoreBase):
        __tablename__ = 'customer'
        name: Mapped[str]
        ...
    # Definir una tabla en la capa Staging:
    class Customer(StagingBase):
        __tablename__ = 'customer'
        name: Mapped[str]
        ...
"""

from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, declared_attr
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER, DATETIME2
from sqlalchemy import Index, text, event, Table, Connection
from uuid import UUID
from datetime import datetime
from bcsync.db.models.metadata import metadata


class Base(DeclarativeBase):
    """
    Clase base del ORM sqlalchemy.
    Inyecta el registro de metadatos global (`metadata`) para centralizar la definición del esquema."""
    metadata = metadata
    pass


class BCSystemFieldsMixin:
    """
        Clase Mixin que define los 'system fields' que están presentes en todas las tablas de Business Central.
        Documentación oficial de microsoft:
        https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-table-system-fields.
    """
    system_id: Mapped[UUID] = mapped_column(
        UNIQUEIDENTIFIER(as_uuid=True),
        nullable=False,
        sort_order=999
    )
    system_created_at: Mapped[datetime] = mapped_column(
        DATETIME2(precision=7, timezone=False),
        nullable=False,
        sort_order=999
    )
    system_modified_at: Mapped[datetime] = mapped_column(
        DATETIME2(precision=7, timezone=False),
        nullable=False,
        sort_order=999
    )

    system_created_by_id: Mapped[UUID] = mapped_column(
        UNIQUEIDENTIFIER(as_uuid=True),
        nullable=True,
        sort_order=999
    )
    system_modified_by_id: Mapped[UUID] = mapped_column(
        UNIQUEIDENTIFIER(as_uuid=True),
        nullable=True,
        sort_order=999
    )


class DWAuditFieldsMixin:
    """
    Clase Mixin que define los campos de auditoría propios del Data Warehouse.

    - created_at: Generado por SQL Server (SYSUTCDATETIME) al insertar.

    - modified_at: Inicializado al insertar. Su actualización posterior es responsabilidad del Stored Procedure de carga (MERGE), no de SQLAlchemy.

    """
    created_at: Mapped[datetime] = mapped_column(
        DATETIME2(precision=7, timezone=False),
        server_default=text("SYSUTCDATETIME()"),
        nullable=False,
        sort_order=1000
    )
    modified_at: Mapped[datetime] = mapped_column(
        DATETIME2(precision=7, timezone=False),
        server_default=text("SYSUTCDATETIME()"),
        nullable=False,
        sort_order=1000
    )


# noinspection PyMethodParameters
class StagingBase(Base, BCSystemFieldsMixin):
    """Clase base abstracta para todos los modelos de la capa staging.
    Cualquier modelo de staging debe de heredar de esta clase, lo cual garantiza:

    - heredar la condición de PK Lógica en system_id, y no tener PK real, ya que todas las tablas de staging conceptualmente son heaps para agilizar el bulk insert.

    - heredar el esquema, por lo que la tabla será definida dentro del esquema 'staging'.
    """
    __abstract__ = True
    __mapper_args__ = {
        "primary_key": [BCSystemFieldsMixin.system_id]  # logical PK on staging, not enforced
    }

    @declared_attr
    def __table_args__(cls):
        return (
            {"schema": "staging"},
        )


# noinspection PyMethodParameters
class CoreBase(Base, BCSystemFieldsMixin, DWAuditFieldsMixin):
    """Clase base abstracta para todos los modelos de la capa core.
    Cualquier modelo del esquema core (DW) debe de heredar de esta clase, lo cual garantiza:

    - heredar la PK física (surrogate key) id INT IDENTITY
    - heredar los índices en system_id y system_modified_at
    - poder agregar más índices específicos de cada subclase, definiendo el atributo __additional_indexes__ como una tupla de objetos Index.
    - todas las subclases tendrán FKs desactivadas vía event listener, sin embargo se puede hacer override definiendo el atributo __enforce_fk_constraints__ = True
    """
    __abstract__ = True
    __enforce_fk_constraints__ = False

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, sort_order=-1)

    @declared_attr
    def __table_args__(cls):
        base_indexes = (
            Index(None, "system_id", unique=True),
            Index(None, "system_modified_at"),
        )

        additional_indexes = getattr(cls, '__additional_indexes__', ())

        enforce_fk_constraints = getattr(cls, '__enforce_fk_constraints__', False)
        return base_indexes + additional_indexes + (
            {
                'schema': "core",
                'info': {'enforce_fk_constraints': enforce_fk_constraints},
            },
        )


#logical FKs on core by default, not enforced
def disable_fks_listener(target: Table, connection: Connection, **kw):
    """
        Event Listener ejecutado después de crear todas las tablas.

        Ejecuta la sentencia `ALTER TABLE ... NOCHECK CONSTRAINT ALL` en todas las tablas de la capa Core (DW).

        Motivación:

        - Permitir la carga de 'Late Arriving Dimensions' en el DW.

        - Mejorar el rendimiento del bulk insert.

        - Mantener la metadata de relaciones visible para herramientas como Power BI.
        """
    if target.info.get('enforce_fk_constraints'):
        return
    table_name = f"[{target.schema or 'dbo'}].[{target.name}]"
    connection.execute(text(f"ALTER TABLE {table_name} NOCHECK CONSTRAINT ALL"))


event.listen(Base.metadata, 'after_create', disable_fks_listener)
