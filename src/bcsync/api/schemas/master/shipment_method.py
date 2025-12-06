from pydantic import Field
from typing import Optional
from bcsync.api.schemas.base import BCEntityModel
from bcsync.api.schemas.types import BCString


class ShipmentMethod(BCEntityModel):
    code: str
    name: BCString = Field(alias='description')