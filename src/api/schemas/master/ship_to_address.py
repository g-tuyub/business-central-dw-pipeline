from typing import Optional
from pydantic import Field
from api.schemas.base import BCEntityModel


class ShipToAddress(BCEntityModel):
    code: str
    customer_code: str = Field(alias='customerNo')
    country_code: Optional[str] = Field(default=None, alias='countryCode')
    city: Optional[str] = None
    postal_code: Optional[str] = Field(default=None, alias='postCode')
    address_line_1: Optional[str] = Field(default=None, alias='address')
    address_line_2: Optional[str] = Field(default=None, alias='address2')
