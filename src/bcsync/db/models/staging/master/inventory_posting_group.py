from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from bcsync.db.models.base import StagingBase


class InventoryPostingGroup(StagingBase):
    __tablename__ = "inventory_posting_group"

    code: Mapped[str] = mapped_column(String(10), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=True)