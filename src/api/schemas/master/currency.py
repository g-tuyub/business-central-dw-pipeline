from pydantic import Field
from api.schemas.base import BCEntityModel


class Currency(BCEntityModel):
    code: str
    name: str = Field(alias='description')
    iso_code: str = Field(alias='isoCode')
