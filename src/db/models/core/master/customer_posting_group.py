from sqlalchemy import String, Index
from sqlalchemy.orm import Mapped, mapped_column
from db.models.base import Base, SystemFieldsMixin, SurrogateKeyMixin

class CustomerPostingGroup(SurrogateKeyMixin, Base, SystemFieldsMixin):
    __tablename__ = "customer_posting_group"
    __table_args__ = (Index(None, "system_id", unique=True, mssql_clustered=False), {"schema": "core"})

    code: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String(100), nullable=True)