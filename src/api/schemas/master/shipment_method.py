from pydantic import Field
from typing import Optional
from api.schemas.base import BCEntityModel


class ShipmentMethod(BCEntityModel):
    code: str
    name: Optional[str] = Field(alias='description')