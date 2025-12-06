from pydantic import Field
from bcsync.api.schemas.base import BCEntityModel
from bcsync.api.schemas.types import BCString
from typing import Optional
from datetime import date


class ExchangeRate(BCEntityModel):
    currency_code : BCString = Field(alias="currencyCode")
    starting_date: date = Field(alias='startingDate')
    relational_currency_code: BCString = Field(alias='relationalCurrencyCode')
    exchange_rate_amount: float = Field(alias='relationalExchRateAmount')
