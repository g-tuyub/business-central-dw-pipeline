from sqlalchemy import String, Index
from sqlalchemy.orm import Mapped, mapped_column
from db.models.base import Base, SystemFieldsMixin


class VendorPostingGroup(Base, SystemFieldsMixin):
    __tablename__ = "vendor_posting_group"
    __table_args__ = (
        Index(None, "system_id", unique=True, mssql_clustered=True),
        {"schema": "staging"}
    )
    __mapper_args__ = {"primary_key": [SystemFieldsMixin.system_id]}

    code: Mapped[str] = mapped_column(String(20), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=True)