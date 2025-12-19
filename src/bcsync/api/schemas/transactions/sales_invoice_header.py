from bcsync.api.schemas.base import BCEntityBase
from bcsync.api.schemas.types import BCString, BCDecimal
from datetime import date
from pydantic import Field
from typing import Optional


class SalesInvoiceHeader(BCEntityBase):
    document_no: str = Field(alias="documentNo")
    posting_date: Optional[date] = Field(alias="postingDate")
    document_date: Optional[date] = Field(alias="documentDate")
    shipment_date: Optional[date] = Field(alias="shipmentDate")
    sell_to_customer_code: BCString = Field(alias="sellToCustomerNo")
    bill_to_customer_code: BCString = Field(alias="billToCustomerNo")
    ship_to_address_code: BCString = Field(alias="shipToCode")
    shipment_method_code: BCString = Field(alias="shipmentMethodCode")
    location_code: BCString = Field(alias="locationCode")
    salesperson_code: BCString = Field(alias="salespersonCode")
    dimension_1_code: BCString = Field(alias="shortcutDimension1Code")
    dimension_2_code: BCString = Field(alias="shortcutDimension2Code")
    currency_code: BCString = Field(alias="currencyCode")
    payment_term_code: BCString = Field(alias="paymentTermsCode")
    payment_method_code: BCString = Field(alias="paymentMethodCode")
    order_no: BCString = Field(alias="orderNo")
    external_document_no: BCString = Field(alias="externalDocumentNo")
    applies_to_document_no: BCString = Field(alias="appliesToDocumentNo")
    no_series: BCString = Field(alias="noSeries")
    customer_ledger_entry_no: Optional[int] = Field(alias="custLedgerEntryNo")
    amount: BCDecimal
    amount_including_vat: BCDecimal = Field(alias="amountIncludingVAT")
    invoice_discount_amount: BCDecimal = Field(alias="invoiceDiscountAmount")
    remaining_amount: BCDecimal = Field(alias="remainingAmount")
    cancelled: Optional[bool]
    reversed: Optional[bool]