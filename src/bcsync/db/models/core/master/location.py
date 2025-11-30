from sqlalchemy import String, Integer, Index
from sqlalchemy.orm import Mapped, mapped_column
from bcsync.db.models.base import CoreBase


class Location(CoreBase):
    __tablename__ = "location"
    __additional_indexes__ = (
        Index(None, "code", unique=True),
    )

    code: Mapped[str] = mapped_column(String(20), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=True)
    postal_code: Mapped[str] = mapped_column(String(20), nullable=True)
    address_line_1: Mapped[str] = mapped_column(String(100), nullable=True)
    address_line_2: Mapped[str] = mapped_column(String(50), nullable=True)
    country_id: Mapped[int] = mapped_column(Integer, nullable=True, index=True)
    country_code: Mapped[str] = mapped_column(String(10), nullable=True)
