from pydantic import Field
from typing import Optional
from bcsync.api.schemas.base import BCEntityModel


class ShipmentMethod(BCEntityModel):
    code: str
    name: Optional[str] = Field(alias='description')