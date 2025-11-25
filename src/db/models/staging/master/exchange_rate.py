from sqlalchemy import String, Date, Float, Index
from sqlalchemy.orm import Mapped, mapped_column
from db.models.base import Base, SystemFieldsMixin


class ExchangeRate(Base, SystemFieldsMixin):
    __tablename__ = "exchange_rate"
    __table_args__ = (
        Index(None, "system_id", unique=True, mssql_clustered=True),
        {"schema": "staging"}
    )
    __mapper_args__ = {"primary_key": [SystemFieldsMixin.system_id]}

    currency_code: Mapped[str] = mapped_column(String(10), nullable=False)
    starting_date: Mapped[Date] = mapped_column(Date, nullable=False)
    relational_currency_code: Mapped[str] = mapped_column(String(10), nullable=True)
    exchange_rate_amount: Mapped[float] = mapped_column(Float, nullable=False)