from pydantic import Field
from typing import Optional
from bcsync.api.schemas.base import BCEntityBase
from bcsync.api.schemas.types import BCString


class CustomerPostingGroup(BCEntityBase):
    code: str
    name: BCString = Field(alias='description')