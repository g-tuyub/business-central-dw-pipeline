from datetime import date
from typing import Optional
from pydantic import Field
from bcsync.api.schemas.base import BCEntityBase
from bcsync.api.schemas.types import BCString, BCDecimal


class SalesInvoiceLine(BCEntityBase):
    line_no: int = Field(alias="lineNo")
    document_no: str = Field(alias="documentNo")
    line_type: BCString = Field(alias="type")
    line_object_code: BCString = Field(alias="no")
    location_code: BCString = Field(alias="locationCode")
    quantity: Optional[BCDecimal] = Field(alias="quantity")
    unit_price: Optional[BCDecimal] = Field(alias="unitPrice")
    amount: Optional[BCDecimal] = Field(alias="amount")
    amount_including_vat: Optional[BCDecimal] = Field(alias="amountIncludingVAT")
    vat_percentage: Optional[BCDecimal] = Field(alias="vatPercentage")
    line_discount_percentage: Optional[BCDecimal] = Field(alias="lineDiscountPercentage")
    line_discount_amount: Optional[BCDecimal] = Field(alias="lineDiscountAmount")
    dimension_1_code: BCString = Field(alias="shortcutDimension1Code")
    dimension_2_code: BCString = Field(alias="shortcutDimension2Code")
    shipment_no: BCString = Field(alias="shipmentNo")
    shipment_line_no: Optional[int] = Field(alias="shipmentLineNo")
    shipment_date: Optional[date] = Field(alias="shipmentDate")
    drop_shipment: Optional[bool] = Field(alias="dropShipment")
    order_no: BCString = Field(alias="orderNo")
    order_line_no: Optional[int] = Field(alias="orderLineNo")
