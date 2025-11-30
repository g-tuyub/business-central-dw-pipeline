from typing import Optional
from pydantic import Field
from api.schemas.base import BCEntityModel


class ItemCategory(BCEntityModel):
    code: str = Field(alias='code')
    name: Optional[str] = Field(alias='description')
    parent_category_code: Optional[str] = Field(alias='parentCategory')
    has_children: bool = Field(alias='hasChildren')