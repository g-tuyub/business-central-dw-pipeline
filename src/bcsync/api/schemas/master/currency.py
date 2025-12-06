from pydantic import Field
from bcsync.api.schemas.base import BCEntityModel
from bcsync.api.schemas.types import BCString


class Currency(BCEntityModel):
    code: str
    name: BCString = Field(alias='description')
    iso_code: BCString = Field(alias='isoCode')
