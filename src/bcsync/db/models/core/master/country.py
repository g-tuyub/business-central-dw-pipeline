from sqlalchemy.orm import Mapped, mapped_column
from bcsync.db.models.base import CoreBase
from sqlalchemy import String


class Country(CoreBase):
    __tablename__ = 'country'

    code: Mapped[str] = mapped_column(String(10), nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=True)

