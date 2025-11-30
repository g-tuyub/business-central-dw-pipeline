from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from db.models.base import StagingBase


class CustomerPriceGroup(StagingBase):
    __tablename__ = "customer_price_group"

    code: Mapped[str] = mapped_column(String(20), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=True)