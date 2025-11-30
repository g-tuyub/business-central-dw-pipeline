from typing import Optional
from pydantic import Field
from bcsync.api.schemas.base import BCEntityModel


class Salesperson(BCEntityModel):
    code: str
    name: Optional[str] = None
    job_title: Optional[str] = Field(default=None, alias='jobTitle')
    dimension_1_code: Optional[str] = Field(default=None, alias='globalDimension1Code')
    dimension_2_code: Optional[str] = Field(default=None, alias='globalDimension2Code')
    blocked: Optional[bool]
