from typing import Optional
from pydantic import Field
from api.schemas.base import BaseEntity


class VendorPostingGroup(BaseEntity):
    code: str
    name: Optional[str] = Field(alias='description')