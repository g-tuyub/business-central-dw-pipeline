from sqlalchemy import String, Integer, Index, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from db.models.base import CoreBase


class ShipToAddress(CoreBase):
    __tablename__ = "ship_to_address"
    __additional_indexes__ = (
        UniqueConstraint("customer_id", "code"),
    )


    code: Mapped[str] = mapped_column(String(20), nullable=False)
    customer_id: Mapped[int] = mapped_column(Integer, nullable=True, index=True)
    customer_code: Mapped[str] = mapped_column(String(20), nullable=False)
    country_id: Mapped[int] = mapped_column(Integer, nullable=True, index=True)
    country_code: Mapped[str] = mapped_column(String(10), nullable=True)
    city: Mapped[str] = mapped_column(String(50), nullable=True)
    postal_code: Mapped[str] = mapped_column(String(20), nullable=True)
    address_line_1: Mapped[str] = mapped_column(String(100), nullable=True)
    address_line_2: Mapped[str] = mapped_column(String(50), nullable=True)
