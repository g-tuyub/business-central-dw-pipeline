from sqlalchemy import String, Index
from sqlalchemy.orm import Mapped, mapped_column
from db.models.base import CoreBase


class VendorPostingGroup(CoreBase):
    __tablename__ = "vendor_posting_group"
    __additional_indexes__ = (
        Index(None, "code", unique=True),
    )

    code: Mapped[str] = mapped_column(String(20), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=True)