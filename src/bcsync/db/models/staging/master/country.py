from sqlalchemy.orm import Mapped, mapped_column
from bcsync.db.models.base import StagingBase
from sqlalchemy import String

class Country(StagingBase):
    __tablename__ = 'country'

    code : Mapped[String] = mapped_column(String(10),nullable=False)
    name : Mapped[String] = mapped_column(String(50),nullable=True)
