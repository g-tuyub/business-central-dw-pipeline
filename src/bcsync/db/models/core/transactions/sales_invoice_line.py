from decimal import Decimal
from datetime import date
from sqlalchemy import String, Date, Numeric, Integer, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from bcsync.db.models.base import CoreBase
from bcsync.db.schemas import DBSchemas


class SalesInvoiceLine(CoreBase):
    __tablename__ = "sales_invoice_line"

    line_no: Mapped[int] = mapped_column(Integer, nullable=False)
    document_no: Mapped[str] = mapped_column(String(20), nullable=False)
    sales_invoice_header_id: Mapped[int] = mapped_column(Integer, ForeignKey(f'{DBSchemas.CORE}.sales_invoice_header.id'), nullable=False, index=True)
    line_type: Mapped[str] = mapped_column(String(20), nullable=True)
    line_object_code: Mapped[str] = mapped_column(String(20), nullable=True)
    item_id: Mapped[int] = mapped_column(Integer, ForeignKey(f'{DBSchemas.CORE}.item.id'), nullable=True,index=True)
    location_code: Mapped[str] = mapped_column(String(10), nullable=True)
    location_id: Mapped[int] = mapped_column(Integer, ForeignKey(f'{DBSchemas.CORE}.location.id'), nullable=True, index=True)
    quantity: Mapped[Decimal] = mapped_column(Numeric(38, 5), nullable=True)
    unit_price: Mapped[Decimal] = mapped_column(Numeric(38, 5), nullable=True)
    amount: Mapped[Decimal] = mapped_column(Numeric(38, 5), nullable=True)
    amount_including_vat: Mapped[Decimal] = mapped_column(Numeric(38, 5), nullable=True)
    vat_percentage: Mapped[Decimal] = mapped_column(Numeric(38, 5), nullable=True)
    line_discount_percentage: Mapped[Decimal] = mapped_column(Numeric(38, 5), nullable=True)
    line_discount_amount: Mapped[Decimal] = mapped_column(Numeric(38, 5), nullable=True)
    dimension_1_code: Mapped[str] = mapped_column(String(20), nullable=True)
    dimension_2_code: Mapped[str] = mapped_column(String(20), nullable=True)
    shipment_no: Mapped[str] = mapped_column(String(20), nullable=True)
    shipment_line_no: Mapped[int] = mapped_column(Integer, nullable=True)
    shipment_date: Mapped[date] = mapped_column(Date, nullable=True)
    drop_shipment: Mapped[bool] = mapped_column(Boolean, nullable=True)
    order_no: Mapped[str] = mapped_column(String(20), nullable=True)
    order_line_no: Mapped[int] = mapped_column(Integer, nullable=True)
