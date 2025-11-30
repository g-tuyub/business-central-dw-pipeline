from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from bcsync.db.models.base import StagingBase


class ShipmentMethod(StagingBase):
    __tablename__ = "shipment_method"

    code: Mapped[str] = mapped_column(String(20), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=True)
