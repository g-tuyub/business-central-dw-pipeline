from typing import Optional
from pydantic import Field
from bcsync.api.schemas.base import BCEntityModel
from bcsync.api.schemas.types import BCString


class Salesperson(BCEntityModel):
    code: str
    name: BCString = None
    job_title: BCString = Field(alias='jobTitle')
    dimension_1_code: BCString = Field(alias='globalDimension1Code')
    dimension_2_code: BCString = Field(alias='globalDimension2Code')
    blocked: Optional[bool]
