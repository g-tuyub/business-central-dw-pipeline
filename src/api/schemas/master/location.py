from typing import Optional
from pydantic import Field
from api.schemas.base import BCEntityModel


class Location(BCEntityModel):
    code: str
    name: Optional[str]
    country_code: Optional[str] = Field(default=None, alias='countryCode')
    postal_code: Optional[str] = Field(default=None, alias='postCode')
    address_line_1: Optional[str] = Field(default=None, alias='address')
    address_line_2: Optional[str] = Field(default=None, alias='address2')
