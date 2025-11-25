from typing import Optional
from pydantic import Field
from api.schemas.base import BaseEntity


class InventoryPostingGroup(BaseEntity):
    code: str = Field(alias='code')
    name: Optional[str] = Field(alias='description')