from bcsync.api.schemas.base import BCEntityModel
from bcsync.api.schemas.types import BCString
from typing import Optional
from pydantic import Field


class Customer(BCEntityModel):
    code: str = Field(alias='no')
    name: BCString
    customer_posting_group_code: BCString = Field(alias='customerPostingGroup')
    customer_price_group_code: BCString = Field(alias='customerPriceGroup')
    currency_code: BCString = Field(alias='currencyCode')
    payment_term_code: BCString = Field(alias='paymentTermsCode')
    payment_method_code: BCString = Field(alias='paymentMethodCode')
    salesperson_code: BCString = Field(alias='salespersonCode')
    shipment_method_code: BCString = Field(alias='shipmentMethodCode')
    location_code: BCString = Field(alias='locationCode')
    address_line_1: BCString = Field(alias='address')
    address_line_2: BCString = Field(alias='address2')
    postal_code: BCString = Field(alias='postCode')
    country_code: BCString = Field(alias='countryCode')
    ship_to_address_code: BCString = Field(alias='shipToCode')
    credit_limit: Optional[float] = Field(alias='creditLimit')
    combine_shipments: Optional[bool] = Field(alias='combineShipments')
    dimension_1_code: BCString = Field(alias='globalDimension1Code')
    dimension_2_code: BCString = Field(alias='globalDimension2Code')
    blocked: BCString
    priority: int

