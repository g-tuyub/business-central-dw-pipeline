from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from bcsync.db.models.base import StagingBase


class ShipToAddress(StagingBase):
    __tablename__ = "ship_to_address"

    code: Mapped[str] = mapped_column(String(20), nullable=False)
    customer_code: Mapped[str] = mapped_column(String(20), nullable=False)
    country_code: Mapped[str] = mapped_column(String(10), nullable=True)
    city: Mapped[str] = mapped_column(String(50), nullable=True)
    postal_code: Mapped[str] = mapped_column(String(20), nullable=True)
    address_line_1: Mapped[str] = mapped_column(String(100), nullable=True)
    address_line_2: Mapped[str] = mapped_column(String(50), nullable=True)