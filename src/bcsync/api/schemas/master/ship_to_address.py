from typing import Optional
from pydantic import Field
from bcsync.api.schemas.base import BCEntityBase
from bcsync.api.schemas.types import BCString


class ShipToAddress(BCEntityBase):
    code: str
    customer_code: str = Field(alias='customerNo')
    country_code: BCString = Field(alias='countryCode')
    city: BCString
    postal_code: BCString = Field(alias='postCode')
    address_line_1: BCString = Field(alias='address')
    address_line_2: BCString = Field(alias='address2')
