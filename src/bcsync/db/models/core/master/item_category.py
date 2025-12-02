from sqlalchemy import String, Boolean, Integer, Index
from sqlalchemy.orm import Mapped, mapped_column
from bcsync.db.models.base import CoreBase


class ItemCategory(CoreBase):
    __tablename__ = "item_category"


    code: Mapped[str] = mapped_column(String(20), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=True)
    parent_category_id: Mapped[int] = mapped_column(Integer, nullable=True,index=True)
    parent_category_code: Mapped[str] = mapped_column(String(20), nullable=True)
    has_children: Mapped[bool] = mapped_column(Boolean)
