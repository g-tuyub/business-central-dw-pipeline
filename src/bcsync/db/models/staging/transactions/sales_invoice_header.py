from datetime import date
from sqlalchemy import String, Date, Numeric, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from bcsync.db.models.base import StagingBase

class SalesInvoiceHeader(StagingBase):
    __tablename__ = "sales_invoice_header"

    document_no: Mapped[str] = mapped_column(String(20), nullable=False)
    posting_date: Mapped[date] = mapped_column(Date, nullable=True)
    document_date: Mapped[date] = mapped_column(Date, nullable=True)
    shipment_date: Mapped[date] = mapped_column(Date, nullable=True)
    sell_to_customer_code: Mapped[str] = mapped_column(String(20), nullable=True)
    bill_to_customer_code: Mapped[str] = mapped_column(String(20), nullable=True)
    ship_to_code: Mapped[str] = mapped_column(String(20), nullable=True)
    shipment_method_code: Mapped[str] = mapped_column(String(20), nullable=True)
    location_code: Mapped[str] = mapped_column(String(20), nullable=True)
    salesperson_code: Mapped[str] = mapped_column(String(20), nullable=True)
    dimension_1_code: Mapped[str] = mapped_column(String(20), nullable=True)
    dimension_2_code: Mapped[str] = mapped_column(String(20), nullable=True)
    currency_code: Mapped[str] = mapped_column(String(10), nullable=True)
    payment_term_code: Mapped[str] = mapped_column(String(20), nullable=True)
    payment_method_code: Mapped[str] = mapped_column(String(20), nullable=True)
    order_no: Mapped[str] = mapped_column(String(20), nullable=True)
    external_document_no: Mapped[str] = mapped_column(String(35), nullable=True)
    applies_to_document_no: Mapped[str] = mapped_column(String(20), nullable=True)
    no_series: Mapped[str] = mapped_column(String(20), nullable=True)
    customer_ledger_entry_no: Mapped[int] = mapped_column(Integer, nullable=False)
    amount: Mapped[float] = mapped_column(Numeric(38, 5), nullable=True)
    amount_including_vat: Mapped[float] = mapped_column(Numeric(38, 5), nullable=True)
    invoice_discount_amount: Mapped[float] = mapped_column(Numeric(38, 5), nullable=True)
    remaining_amount: Mapped[float] = mapped_column(Numeric(38, 5), nullable=True)
    cancelled: Mapped[bool] = mapped_column(Boolean, nullable=True)
    reversed: Mapped[bool] = mapped_column(Boolean, nullable=True)