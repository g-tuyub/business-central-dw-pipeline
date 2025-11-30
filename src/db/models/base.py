from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, declared_attr
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER, DATETIME2
from sqlalchemy import Index
from uuid import UUID
from datetime import datetime
from db.models.metadata import metadata


class Base(DeclarativeBase):
    metadata = metadata
    pass


class SystemFieldsMixin:
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


# noinspection PyMethodParameters
class StagingBase(Base, SystemFieldsMixin):
    __abstract__ = True
    __mapper_args__ = {
        "primary_key": [SystemFieldsMixin.system_id]  # logical PK, not enforced
    }


    @declared_attr
    def __table_args__(cls):
        return (
            {"schema": "staging"},
        )


# noinspection PyMethodParameters
class CoreBase(Base, SystemFieldsMixin):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True,sort_order=-1)

    @declared_attr
    def __table_args__(cls):

        base_indexes = (
            Index(None,"system_id", unique=True),
            Index(None,"system_modified_at"),
        )

        additional_indexes = getattr(cls,'__additional_indexes__',())

        return base_indexes + additional_indexes + ({"schema" : "core"},)