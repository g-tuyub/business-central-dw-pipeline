from typing import Optional
from pydantic import Field
from bcsync.api.schemas.base import BCEntityModel
from bcsync.api.schemas.types import BCString


class ItemCategory(BCEntityModel):
    code: str = Field(alias='code')
    name: BCString = Field(alias='description')
    parent_category_code: BCString = Field(alias='parentCategory')
    has_children: bool = Field(alias='hasChildren')