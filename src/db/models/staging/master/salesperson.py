from sqlalchemy import String, Boolean, Index
from sqlalchemy.orm import Mapped, mapped_column
from db.models.base import Base, SystemFieldsMixin


class Salesperson(Base, SystemFieldsMixin):
    __tablename__ = "salesperson"
    __table_args__ = (
        Index(None, "system_id", unique=True, mssql_clustered=True),
        {"schema": "staging"}
    )
    __mapper_args__ = {
        "primary_key": [SystemFieldsMixin.system_id]
    }

    code: Mapped[str] = mapped_column(String(20), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=True)
    job_title: Mapped[str] = mapped_column(String(50), nullable=True)
    dimension_1_code: Mapped[str] = mapped_column(String(20), nullable=True)
    dimension_2_code: Mapped[str] = mapped_column(String(20), nullable=True)
    blocked: Mapped[bool] = mapped_column(Boolean, nullable=True)