from typing import Optional
from pydantic import Field
from bcsync.api.schemas.base import BCEntityBase
from bcsync.api.schemas.types import BCString


class InventoryPostingGroup(BCEntityBase):
    code: str = Field(alias='code')
    name: BCString = Field(alias='description')