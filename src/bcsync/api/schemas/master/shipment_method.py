from pydantic import Field
from typing import Optional
from bcsync.api.schemas.base import BCEntityBase
from bcsync.api.schemas.types import BCString


class ShipmentMethod(BCEntityBase):
    code: str
    name: BCString = Field(alias='description')