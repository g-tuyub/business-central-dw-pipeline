from sqlalchemy import String, Integer, Index, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from db.models.base import Base, SystemFieldsMixin, SurrogateKeyMixin


class Location(SurrogateKeyMixin, Base, SystemFieldsMixin):
    __tablename__ = "location"

    __table_args__ = (
        Index(None, "system_id", unique=True, mssql_clustered=False),
        {"schema": "core"}
    )

    code: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String(100), nullable=True)
    postal_code: Mapped[str] = mapped_column(String(20), nullable=True)
    address_line_1: Mapped[str] = mapped_column(String(100), nullable=True)
    address_line_2: Mapped[str] = mapped_column(String(50), nullable=True)
    country_code: Mapped[str] = mapped_column(String(10), nullable=True)
    country_id: Mapped[int] = mapped_column(Integer, ForeignKey("core.country.id"), nullable=True)