from typing import Optional
from pydantic import Field
from bcsync.api.schemas.base import BCEntityModel


class InventoryPostingGroup(BCEntityModel):
    code: str = Field(alias='code')
    name: Optional[str] = Field(alias='description')