from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from ...base import StagingBase


class Location(StagingBase):
    __tablename__ = "location"

    code: Mapped[str] = mapped_column(String(20), nullable=False)  # BC Code standard length
    name: Mapped[str] = mapped_column(String(100), nullable=True)
    postal_code: Mapped[str] = mapped_column(String(20), nullable=True)
    address_line_1: Mapped[str] = mapped_column(String(100), nullable=True)
    address_line_2: Mapped[str] = mapped_column(String(50), nullable=True)
    country_code: Mapped[str] = mapped_column(String(10), nullable=True)
