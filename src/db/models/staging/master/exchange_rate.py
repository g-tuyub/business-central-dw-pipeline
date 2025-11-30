from sqlalchemy import String, Date, Float
from sqlalchemy.orm import Mapped, mapped_column
from db.models.base import StagingBase


class ExchangeRate(StagingBase):
    __tablename__ = "exchange_rate"

    currency_code: Mapped[str] = mapped_column(String(10), nullable=False)
    starting_date: Mapped[Date] = mapped_column(Date, nullable=False)
    relational_currency_code: Mapped[str] = mapped_column(String(10), nullable=True)
    exchange_rate_amount: Mapped[float] = mapped_column(Float, nullable=False)