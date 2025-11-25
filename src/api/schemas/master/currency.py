from pydantic import Field
from api.schemas.base import BaseEntity


class Currency(BaseEntity):
    code: str
    name: str = Field(alias='description')
    iso_code: str = Field(alias='isoCode')
