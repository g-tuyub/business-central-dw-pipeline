from pydantic import Field
from api.schemas.base import BaseEntity
from typing import Optional
from datetime import date


class ExchangeRate(BaseEntity):
    currency_code : str = Field(alias="currencyCode")
    starting_date: date = Field(alias='startingDate')
    relational_currency_code: Optional[str] = Field(default=None, alias='relationalCurrencyCode')
    exchange_rate_amount: float = Field(alias='relationalExchRateAmount')
