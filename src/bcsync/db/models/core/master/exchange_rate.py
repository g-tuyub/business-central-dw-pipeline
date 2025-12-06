from sqlalchemy import Date, Float, Integer, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from bcsync.db.models.base import CoreBase, DBSchemas


class ExchangeRate(CoreBase):
    __tablename__ = "exchange_rate"

    currency_id: Mapped[int] = mapped_column(Integer, ForeignKey(f'{DBSchemas.CORE}.currency.id'), nullable=False, index=True)
    currency_code: Mapped[str] = mapped_column(String(10), nullable=False)
    starting_date: Mapped[Date] = mapped_column(Date, nullable=False)
    relational_currency_id: Mapped[int] = mapped_column(Integer, ForeignKey(f'{DBSchemas.CORE}.currency.id'), nullable=True, index=True)
    relational_currency_code: Mapped[str] = mapped_column(String(10), nullable=True)
    exchange_rate_amount: Mapped[float] = mapped_column(Float, nullable=False)