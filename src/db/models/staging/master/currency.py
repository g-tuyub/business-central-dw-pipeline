from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from db.models.base import StagingBase

class Currency(StagingBase):
    __tablename__ = "currency"

    code: Mapped[str] = mapped_column(String(10), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=True)
    iso_code: Mapped[str] = mapped_column(String(10), nullable=True)