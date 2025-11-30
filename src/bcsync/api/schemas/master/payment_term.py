from typing import Optional
from pydantic import Field
from bcsync.api.schemas.base import BCEntityModel


class PaymentTerm(BCEntityModel):
    code: str
    name: Optional[str] = Field(alias='description')