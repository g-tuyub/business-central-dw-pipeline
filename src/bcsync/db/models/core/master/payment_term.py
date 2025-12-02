from sqlalchemy import String, Index
from sqlalchemy.orm import Mapped, mapped_column
from bcsync.db.models.base import CoreBase


class PaymentTerm(CoreBase):
    __tablename__ = "payment_term"

    code: Mapped[str] = mapped_column(String(10), nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=True)