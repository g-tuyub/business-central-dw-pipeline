from typing import Optional
from pydantic import Field
from bcsync.api.schemas.base import BCEntityBase
from bcsync.api.schemas.types import BCString


class ItemCategory(BCEntityBase):
    code: str = Field(alias='code')
    name: BCString = Field(alias='description')
    parent_category_code: BCString = Field(alias='parentCategory')
    has_children: bool = Field(alias='hasChildren')