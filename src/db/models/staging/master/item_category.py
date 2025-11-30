from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from db.models.base import StagingBase


class ItemCategory(StagingBase):
    __tablename__ = "item_category"

    code: Mapped[str] = mapped_column(String(20), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=True)
    parent_category_code: Mapped[str] = mapped_column(String(20), nullable=True)
    has_children: Mapped[bool] = mapped_column(Boolean, nullable=True)