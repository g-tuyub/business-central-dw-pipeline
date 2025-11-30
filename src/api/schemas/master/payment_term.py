from typing import Optional
from pydantic import Field
from api.schemas.base import BCEntityModel


class PaymentTerm(BCEntityModel):
    code: str
    name: Optional[str] = Field(alias='description')