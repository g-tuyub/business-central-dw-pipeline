from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from bcsync.db.models.base import CoreBase


class Currency(CoreBase):
    __tablename__ = "currency"

    code: Mapped[str] = mapped_column(String(10), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=True)
    iso_code: Mapped[str] = mapped_column(String(10), nullable=True)