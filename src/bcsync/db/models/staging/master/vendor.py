from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from bcsync.db.models.base import StagingBase


class Vendor(StagingBase):
    __tablename__ = 'vendor'

    code: Mapped[str] = mapped_column(String(20), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=True)
    vendor_posting_group_code: Mapped[str] = mapped_column(String(20), nullable=True)
    currency_code: Mapped[str] = mapped_column(String(10), nullable=True)
    payment_term_code: Mapped[str] = mapped_column(String(20), nullable=True)
    payment_method_code: Mapped[str] = mapped_column(String(20), nullable=True)
    purchaser_code: Mapped[str] = mapped_column(String(20), nullable=True)
    shipment_method_code: Mapped[str] = mapped_column(String(20), nullable=True)
    address_line_1: Mapped[str] = mapped_column(String(100), nullable=True)
    address_line_2: Mapped[str] = mapped_column(String(50), nullable=True)
    postal_code: Mapped[str] = mapped_column(String(20), nullable=True)
    country_code: Mapped[str] = mapped_column(String(10), nullable=True)
    dimension_1_code: Mapped[str] = mapped_column(String(20), nullable=True)
    dimension_2_code: Mapped[str] = mapped_column(String(20), nullable=True)
    blocked: Mapped[str] = mapped_column(String(20), nullable=True)
    priority: Mapped[int] = mapped_column(Integer, nullable=True)
