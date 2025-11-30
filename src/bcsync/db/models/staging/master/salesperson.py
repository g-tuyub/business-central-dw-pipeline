from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from bcsync.db.models.base import StagingBase

class Salesperson(StagingBase):
    __tablename__ = "salesperson"

    code: Mapped[str] = mapped_column(String(20), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=True)
    job_title: Mapped[str] = mapped_column(String(50), nullable=True)
    dimension_1_code: Mapped[str] = mapped_column(String(20), nullable=True)
    dimension_2_code: Mapped[str] = mapped_column(String(20), nullable=True)
    blocked: Mapped[bool] = mapped_column(Boolean, nullable=True)