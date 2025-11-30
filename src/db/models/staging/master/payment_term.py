from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from db.models.base import StagingBase


class PaymentTerm(StagingBase):
    __tablename__ = "payment_term"

    code: Mapped[str] = mapped_column(String(10), nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=True)