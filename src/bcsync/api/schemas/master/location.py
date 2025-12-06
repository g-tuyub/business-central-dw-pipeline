from typing import Optional
from pydantic import Field
from bcsync.api.schemas.base import BCEntityModel
from bcsync.api.schemas.types import BCString


class Location(BCEntityModel):
    code: str
    name: BCString
    country_code: BCString = Field(alias='countryCode')
    postal_code: BCString = Field(alias='postCode')
    address_line_1: BCString = Field(alias='address')
    address_line_2: BCString = Field(alias='address2')
