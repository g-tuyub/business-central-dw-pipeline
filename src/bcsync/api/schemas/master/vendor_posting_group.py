from typing import Optional
from pydantic import Field
from bcsync.api.schemas.base import BCEntityModel


class VendorPostingGroup(BCEntityModel):
    code: str
    name: Optional[str] = Field(alias='description')