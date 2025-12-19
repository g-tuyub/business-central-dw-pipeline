from typing import Optional
from pydantic import Field
from bcsync.api.schemas.base import BCEntityBase
from bcsync.api.schemas.types import BCString, BCDecimal
from datetime import date


class CustomerLedgerEntry(BCEntityBase):
    entry_no: int = Field(alias="entryNo")
    posting_date: Optional[date] = Field(alias="postingDate")
    document_date: Optional[date] = Field(alias="documentDate")
    closed_at_date: Optional[date] = Field(alias="closedAtDate")
    document_no: BCString = Field(alias="documentNo")
    document_type: BCString = Field(alias="documentType")
    external_document_no: BCString = Field(alias="externalDocumentNo")
    applies_to_document_no: BCString = Field(alias="appliestoDocNo")
    customer_code: BCString = Field(alias="customerNo")
    currency_code: BCString = Field(alias="currencyCode")
    dimension_1_code: BCString = Field(alias="globalDimension1Code")
    dimension_2_code: BCString = Field(alias="globalDimension2Code")
    dimension_3_code: BCString = Field(alias="shortcutDimension3Code")
    dimension_4_code: BCString = Field(alias="shortcutDimension4Code")
    dimension_5_code: BCString = Field(alias="shortcutDimension5Code")
    dimension_6_code: BCString = Field(alias="shortcutDimension6Code")
    dimension_7_code: BCString = Field(alias="shortcutDimension7Code")
    dimension_8_code: BCString = Field(alias="shortcutDimension8Code")
    amount: Optional[BCDecimal] = Field(alias="amount")
    original_amount: Optional[BCDecimal] = Field(alias="originalAmount")
    remaining_amount: Optional[BCDecimal] = Field(alias="remainingAmount")
    debit_amount: Optional[BCDecimal] = Field(alias="debitAmount")
    credit_amount: Optional[BCDecimal] = Field(alias="creditAmount")
    sales_lcy: Optional[BCDecimal] = Field(alias="salesLCY")
    profit_lcy: Optional[BCDecimal] = Field(alias="profitLCY")
    open: Optional[bool] = Field(alias="open")
    positive: Optional[bool] = Field(alias="positive")
    reversed: Optional[bool] = Field(alias="reversed")
    closed_by_entry_no: Optional[int] = Field(alias="closedbyEntryNo")
    transaction_no: Optional[int] = Field(alias="transactionNo")
    reversed_by_entry_no: Optional[int] = Field(alias="reversedbyEntryNo")
    reversed_entry_no: Optional[int] = Field(alias="reversedEntryNo")