from sqlalchemy import String, Index
from sqlalchemy.orm import Mapped, mapped_column
from bcsync.db.models.base import CoreBase


class PaymentTerm(CoreBase):
    __tablename__ = "payment_term"
    __additional_indexes__ = (
        Index(None, "code", unique=True),
    )

    code: Mapped[str] = mapped_column(String(10), nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=True)