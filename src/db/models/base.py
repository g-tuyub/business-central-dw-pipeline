from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER, DATETIME2
from uuid import UUID
from datetime import datetime
from .metadata import metadata


class Base(DeclarativeBase):
    metadata = metadata
    pass


class SystemFieldsMixin(DeclarativeBase):
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
        sort_order=999,
        index=True
    )


class SurrogateKeyMixin(DeclarativeBase):
    id : Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        sort_order=-1
    )
