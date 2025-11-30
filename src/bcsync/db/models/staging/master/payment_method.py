from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from bcsync.db.models.base import StagingBase

class PaymentMethod(StagingBase):
    __tablename__ = "payment_method"

    code: Mapped[str] = mapped_column(String(20), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=True)