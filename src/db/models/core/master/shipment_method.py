from sqlalchemy import String, Index
from sqlalchemy.orm import Mapped, mapped_column
from db.models.base import Base, SystemFieldsMixin, SurrogateKeyMixin

class ShipmentMethod(SurrogateKeyMixin, Base, SystemFieldsMixin):
    __tablename__ = "shipment_method"
    __table_args__ = (Index(None, "system_id", unique=True, mssql_clustered=False), {"schema": "core"})

    code: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String(100), nullable=True)