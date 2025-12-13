from pydantic import Field
from bcsync.api.schemas.base import BCEntityBase
from bcsync.api.schemas.types import BCString


class Currency(BCEntityBase):
    code: str
    name: BCString = Field(alias='description')
    iso_code: BCString = Field(alias='isoCode')
