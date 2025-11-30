from typing import Optional
from pydantic import Field
from api.schemas.base import BCEntityModel


class Vendor(BCEntityModel):
    code: str = Field(alias='no')
    name: Optional[str]
    vendor_posting_group_code: Optional[str] = Field(default=None, alias='vendorPostingGroup')
    currency_code: Optional[str] = Field(alias='currencyCode')
    payment_term_code: Optional[str] = Field(alias='paymentTermsCode')
    payment_method_code: Optional[str] = Field(alias='paymentMethodCode')
    purchaser_code: Optional[str] = Field(alias='purchaserCode')
    shipment_method_code: Optional[str] = Field(alias='shipmentMethodCode')
    address_line_1: Optional[str] = Field(default=None, alias='address')
    address_line_2: Optional[str] = Field(default=None, alias='address2')
    postal_code: Optional[str] = Field(default=None, alias='postCode')
    country_code: Optional[str] = Field(default=None, alias='countryCode')
    dimension_1_code: Optional[str] = Field(default=None, alias='globalDimension1Code')
    dimension_2_code: Optional[str] = Field(default=None, alias='globalDimension2Code')
    blocked: Optional[str]
    priority: int