from typing import Optional
from pydantic import Field
from bcsync.api.schemas.base import BCEntityModel
from bcsync.api.schemas.types import BCString


class InventoryPostingGroup(BCEntityModel):
    code: str = Field(alias='code')
    name: BCString = Field(alias='description')