from sqlalchemy import String, Index
from sqlalchemy.orm import Mapped, mapped_column
from ...base import Base, SystemFieldsMixin


class Location(Base, SystemFieldsMixin):
    __tablename__ = "location"
    __table_args__ = (
        Index(None, "system_id", unique=True, mssql_clustered=True),
        {"schema": "staging"}
    )
    __mapper_args__ = {
        "primary_key": [SystemFieldsMixin.system_id]
    }

    code: Mapped[str] = mapped_column(String(20), nullable=False)  # BC Code standard length
    name: Mapped[str] = mapped_column(String(100), nullable=True)
    country_code: Mapped[str] = mapped_column(String(10), nullable=True)
    postal_code: Mapped[str] = mapped_column(String(20), nullable=True)
    address_line_1: Mapped[str] = mapped_column(String(100), nullable=True)
    address_line_2: Mapped[str] = mapped_column(String(50), nullable=True)