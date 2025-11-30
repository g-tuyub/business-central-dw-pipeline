from pydantic import Field
from typing import Optional
from api.schemas.base import BCEntityModel


class CustomerPriceGroup(BCEntityModel):
    code: str
    name: Optional[str] = Field(alias='description')