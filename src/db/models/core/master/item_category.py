from sqlalchemy import String, Boolean, Integer, Index, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.models.base import Base, SystemFieldsMixin, SurrogateKeyMixin


class ItemCategory(SurrogateKeyMixin, Base, SystemFieldsMixin):
    __tablename__ = "item_category"
    __table_args__ = (
        Index(None, "system_id", unique=True, mssql_clustered=False),
        {"schema": "core"}
    )

    code: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String(100), nullable=True)
    parent_category_id: Mapped[int] = mapped_column(Integer, ForeignKey("core.item_category.id"), nullable=True)
    has_children: Mapped[bool] = mapped_column(Boolean)
