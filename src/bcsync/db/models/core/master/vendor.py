from sqlalchemy import String, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column
from bcsync.db.models.base import CoreBase, DBSchemas


class Vendor(CoreBase):
    __tablename__ = "vendor"

    code: Mapped[str] = mapped_column(String(20), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=True)
    vendor_posting_group_id: Mapped[int] = mapped_column(Integer,ForeignKey(f'{DBSchemas.CORE}.vendor_posting_group.id'), nullable=True, index=True)
    vendor_posting_group_code: Mapped[str] = mapped_column(String(20), nullable=True)
    currency_id: Mapped[int] = mapped_column(Integer, ForeignKey(f'{DBSchemas.CORE}.currency.id'),nullable=True, index=True)
    currency_code: Mapped[str] = mapped_column(String(10), nullable=True)
    payment_term_id: Mapped[int] = mapped_column(Integer, ForeignKey(f'{DBSchemas.CORE}.payment_term.id'),nullable=True, index=True)
    payment_term_code: Mapped[str] = mapped_column(String(20), nullable=True)
    payment_method_id: Mapped[int] = mapped_column(Integer, ForeignKey(f'{DBSchemas.CORE}.payment_method.id'), nullable=True, index=True)
    payment_method_code: Mapped[str] = mapped_column(String(20), nullable=True)
    purchaser_id: Mapped[int] = mapped_column(Integer, ForeignKey(f'{DBSchemas.CORE}.salesperson.id'), nullable=True, index=True)
    purchaser_code: Mapped[str] = mapped_column(String(20), nullable=True)
    shipment_method_id: Mapped[int] = mapped_column(Integer, ForeignKey(f'{DBSchemas.CORE}.shipment_method.id'), nullable=True, index=True)
    shipment_method_code: Mapped[str] = mapped_column(String(20), nullable=True)
    address_line_1: Mapped[str] = mapped_column(String(100), nullable=True)
    address_line_2: Mapped[str] = mapped_column(String(50), nullable=True)
    postal_code: Mapped[str] = mapped_column(String(20), nullable=True)
    country_id: Mapped[int] = mapped_column(Integer, ForeignKey(f'{DBSchemas.CORE}.country.id'), nullable=True, index=True)
    country_code: Mapped[str] = mapped_column(String(10), nullable=True)
    dimension_1_code: Mapped[str] = mapped_column(String(20), nullable=True)
    dimension_2_code: Mapped[str] = mapped_column(String(20), nullable=True)
    blocked: Mapped[str] = mapped_column(String(20), nullable=True)
    priority: Mapped[int] = mapped_column(Integer, nullable=True)
