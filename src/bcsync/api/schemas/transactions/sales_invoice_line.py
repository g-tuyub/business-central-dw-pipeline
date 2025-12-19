from decimal import Decimal, ROUND_HALF_UP
from datetime import date
from typing import Optional
from pydantic import Field, field_validator
from bcsync.api.schemas.base import BCEntityBase


class SalesInvoiceLine(BCEntityBase):
    line_no: int = Field(alias="lineNo")
    document_no: str = Field(alias="documentNo")
    line_type: Optional[str] = Field(alias="type")
    line_object_no: Optional[str] = Field(alias="no")
    location_code: Optional[str] = Field(alias="locationCode")
    quantity: Optional[Decimal] = Field(alias="quantity")
    unit_price: Optional[Decimal] = Field(alias="unitPrice")
    amount: Optional[Decimal] = Field(alias="amount")
    amount_including_vat: Optional[Decimal] = Field(alias="amountIncludingVAT")
    vat_percentage: Optional[Decimal] = Field(alias="VATPercentage")
    line_discount_percentage: Optional[Decimal] = Field(alias="lineDiscountPercentage")
    line_discount_amount: Optional[Decimal] = Field(alias="lineDiscountAmount")
    dimension_1_code: Optional[str] = Field(alias="shortcutDimension1Code")
    dimension_2_code: Optional[str] = Field(alias="shortcutDimension2Code")
    shipment_no: Optional[str] = Field(alias="shipmentNo")
    shipment_line_no: Optional[int] = Field(alias="shipmentLineNo")
    shipment_date: Optional[date] = Field(alias="shipmentDate")
    drop_shipment: Optional[bool] = Field(alias="dropShipment")
    order_no: Optional[str] = Field(alias="orderNo")
    order_line_no: Optional[int] = Field(alias="orderLineNo")

    @field_validator(
        'quantity',
        'unit_price',
        'amount',
        'amount_including_vat',
        'vat_percentage',
        'line_discount_percentage',
        'line_discount_amount',
        mode='before'
    )
    @classmethod
    def round_decimals(cls, v):
        if v is None:
            return None
        d = Decimal(str(v))
        return d.quantize(Decimal("0.00001"), rounding=ROUND_HALF_UP)