from pydantic import Field
from bcsync.api.schemas.base import BCEntityModel
from typing import Optional
from datetime import date


class ExchangeRate(BCEntityModel):
    currency_code : str = Field(alias="currencyCode")
    starting_date: date = Field(alias='startingDate')
    relational_currency_code: Optional[str] = Field(default=None, alias='relationalCurrencyCode')
    exchange_rate_amount: float = Field(alias='relationalExchRateAmount')
