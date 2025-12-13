from typing import Optional
from pydantic import Field
from bcsync.api.schemas.base import BCEntityBase
from bcsync.api.schemas.types import BCString


class VendorPostingGroup(BCEntityBase):
    code: str
    name: BCString = Field(alias='description')