from api.schemas.base import BaseEntity
from typing import Optional
from pydantic import Field


class Customer(BaseEntity):
    code: str = Field(alias='no')
    name: Optional[str]
    customer_posting_group_code: Optional[str] = Field(alias='customerPostingGroup')
    customer_price_group_code: Optional[str] = Field(alias='customerPriceGroup')
    currency_code: Optional[str] = Field(alias='currencyCode')
    payment_term_code: Optional[str] = Field(alias='paymentTermsCode')
    payment_method_code: Optional[str] = Field(alias='paymentMethodCode')
    salesperson_code: Optional[str] = Field(alias='salespersonCode')
    shipment_method_code: Optional[str] = Field(alias='shipmentMethodCode')
    location_code: Optional[str] = Field(alias='locationCode')
    address_line_1: Optional[str] = Field(alias='address')
    address_line_2: Optional[str] = Field(alias='address2')
    postal_code: Optional[str] = Field(alias='postCode')
    country_code: Optional[str] = Field(alias='countryCode')
    ship_to_address_code: Optional[str] = Field(alias='shipToCode')
    credit_limit: Optional[float] = Field(alias='creditLimit')
    combine_shipments: Optional[bool] = Field(alias='combineShipments')
    dimension_1_code: Optional[str] = Field(alias='globalDimension1Code')
    dimension_2_code: Optional[str] = Field(alias='globalDimension2Code')

