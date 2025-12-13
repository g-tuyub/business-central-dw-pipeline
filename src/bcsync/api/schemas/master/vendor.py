from typing import Optional
from pydantic import Field
from bcsync.api.schemas.base import BCEntityBase
from bcsync.api.schemas.types import BCString


class Vendor(BCEntityBase):
    code: str = Field(alias='no')
    name: BCString
    vendor_posting_group_code: BCString = Field(alias='vendorPostingGroup')
    currency_code: BCString = Field(alias='currencyCode')
    payment_term_code: BCString = Field(alias='paymentTermsCode')
    payment_method_code: BCString = Field(alias='paymentMethodCode')
    purchaser_code: BCString = Field(alias='purchaserCode')
    shipment_method_code: BCString = Field(alias='shipmentMethodCode')
    address_line_1: BCString = Field(alias='address')
    address_line_2: BCString = Field(alias='address2')
    postal_code: BCString = Field(alias='postCode')
    country_code: BCString = Field(alias='countryCode')
    dimension_1_code: BCString = Field(alias='globalDimension1Code')
    dimension_2_code: BCString = Field(alias='globalDimension2Code')
    blocked: BCString
    priority: int