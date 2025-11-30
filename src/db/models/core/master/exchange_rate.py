from sqlalchemy import Date, Float, Integer,ForeignKey, UniqueConstraint, String
from sqlalchemy.orm import Mapped, mapped_column
from db.models.base import CoreBase


class ExchangeRate(CoreBase):
    __tablename__ = "exchange_rate"
    __additional_indexes__ = (
        UniqueConstraint("currency_code", "starting_date"),
    )

    currency_id: Mapped[int] = mapped_column(Integer, nullable=False, index=True)
    currency_code: Mapped[str] = mapped_column(String(10), nullable=False)
    starting_date: Mapped[Date] = mapped_column(Date, nullable=False)
    relational_currency_id: Mapped[int] = mapped_column(Integer, nullable=True, index=True)
    relational_currency_code: Mapped[str] = mapped_column(String(10), nullable=True)
    exchange_rate_amount: Mapped[float] = mapped_column(Float, nullable=False)