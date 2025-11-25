from pydantic import Field
from typing import Optional
from api.schemas.base import BaseEntity


class CustomerPriceGroup(BaseEntity):
    code: str
    name: Optional[str] = Field(alias='description')