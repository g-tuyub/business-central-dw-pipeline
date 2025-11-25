from sqlalchemy import Date, Float, Integer, Index, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from db.models.base import Base, SystemFieldsMixin, SurrogateKeyMixin


class ExchangeRate(SurrogateKeyMixin, Base, SystemFieldsMixin):
    __tablename__ = "exchange_rate"
    __table_args__ = (
        Index(None, "system_id", unique=True, mssql_clustered=False),
        UniqueConstraint("currency_id", "starting_date"),
        {"schema": "core"}
    )
    currency_id: Mapped[int] = mapped_column(Integer, ForeignKey("core.currency.id"), nullable=False)
    starting_date: Mapped[Date] = mapped_column(Date, nullable=False)
    relational_currency_id: Mapped[int] = mapped_column(Integer, ForeignKey("core.currency.id"), nullable=True)
    exchange_rate_amount: Mapped[float] = mapped_column(Float, nullable=False)