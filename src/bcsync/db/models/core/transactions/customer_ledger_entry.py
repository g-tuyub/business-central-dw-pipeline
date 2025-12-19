from decimal import Decimal
from datetime import date
from sqlalchemy import String, Date, Numeric, Integer, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from bcsync.db.models.base import CoreBase
from bcsync.db.schemas import DBSchemas

class CustomerLedgerEntry(CoreBase):
    __tablename__ = "customer_ledger_entry"

    entry_no: Mapped[int] = mapped_column(Integer, nullable=False)
    posting_date: Mapped[date] = mapped_column(Date, nullable=True)
    document_date: Mapped[date] = mapped_column(Date, nullable=True)
    closed_at_date: Mapped[date] = mapped_column(Date, nullable=True)
    document_no: Mapped[str] = mapped_column(String(20), nullable=True)
    document_type: Mapped[str] = mapped_column(String(20), nullable=True)
    external_document_no: Mapped[str] = mapped_column(String(35), nullable=True)
    applies_to_document_no: Mapped[str] = mapped_column(String(20), nullable=True)
    customer_code: Mapped[str] = mapped_column(String(20), nullable=True)
    customer_id: Mapped[int] = mapped_column(Integer, ForeignKey(f'{DBSchemas.CORE}.customer.id'), nullable=True,index=True)
    currency_code: Mapped[str] = mapped_column(String(10), nullable=True)
    currency_id: Mapped[int] = mapped_column(Integer, ForeignKey(f'{DBSchemas.CORE}.currency.id'), nullable=True, index=True)
    dimension_1_code: Mapped[str] = mapped_column(String(20), nullable=True)
    dimension_2_code: Mapped[str] = mapped_column(String(20), nullable=True)
    dimension_3_code: Mapped[str] = mapped_column(String(20), nullable=True)
    dimension_4_code: Mapped[str] = mapped_column(String(20), nullable=True)
    dimension_5_code: Mapped[str] = mapped_column(String(20), nullable=True)
    dimension_6_code: Mapped[str] = mapped_column(String(20), nullable=True)
    dimension_7_code: Mapped[str] = mapped_column(String(20), nullable=True)
    dimension_8_code: Mapped[str] = mapped_column(String(20), nullable=True)
    amount: Mapped[Decimal] = mapped_column(Numeric(38, 5), nullable=True)
    original_amount: Mapped[Decimal] = mapped_column(Numeric(38, 5), nullable=True)
    remaining_amount: Mapped[Decimal] = mapped_column(Numeric(38, 5), nullable=True)
    debit_amount: Mapped[Decimal] = mapped_column(Numeric(38, 5), nullable=True)
    credit_amount: Mapped[Decimal] = mapped_column(Numeric(38, 5), nullable=True)
    sales_lcy: Mapped[Decimal] = mapped_column(Numeric(38, 5), nullable=True)
    profit_lcy: Mapped[Decimal] = mapped_column(Numeric(38, 5), nullable=True)
    open: Mapped[bool] = mapped_column(Boolean, nullable=True)
    positive: Mapped[bool] = mapped_column(Boolean, nullable=True)
    reversed: Mapped[bool] = mapped_column(Boolean, nullable=True)
    closed_by_entry_no: Mapped[int] = mapped_column(Integer, nullable=True)
    transaction_no: Mapped[int] = mapped_column(Integer, nullable=True)
    reversed_by_entry_no: Mapped[int] = mapped_column(Integer, nullable=True)
    reversed_entry_no: Mapped[int] = mapped_column(Integer, nullable=True)