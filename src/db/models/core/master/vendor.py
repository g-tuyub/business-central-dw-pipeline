from sqlalchemy import String, Index, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from db.models.base import Base, SystemFieldsMixin, SurrogateKeyMixin

class Vendor(SurrogateKeyMixin, Base, SystemFieldsMixin):
    __tablename__ = "vendor"

    __table_args__ = (
        Index(None, "system_id", unique=True, mssql_clustered=False),
        {"schema": "core"}
    )

    code: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String(100), nullable=True)
    vendor_posting_group_id: Mapped[int] = mapped_column(Integer, ForeignKey("core.vendor_posting_group.id"),nullable=True)
    currency_id: Mapped[int] = mapped_column(Integer, ForeignKey("core.currency.id"), nullable=True)
    payment_term_id: Mapped[int] = mapped_column(Integer, ForeignKey("core.payment_term.id"), nullable=True)
    payment_method_id: Mapped[int] = mapped_column(Integer, ForeignKey("core.payment_method.id"), nullable=True)
    purchaser_id: Mapped[int] = mapped_column(Integer, ForeignKey("core.salesperson.id"), nullable=True)
    shipment_method_id: Mapped[int] = mapped_column(Integer, ForeignKey("core.shipment_method.id"), nullable=True)
    address_line_1: Mapped[str] = mapped_column(String(100), nullable=True)
    address_line_2: Mapped[str] = mapped_column(String(50), nullable=True)
    postal_code: Mapped[str] = mapped_column(String(20), nullable=True)
    country_id: Mapped[int] = mapped_column(Integer, ForeignKey("core.country.id"), nullable=True)
    dimension_1_code: Mapped[str] = mapped_column(String(20), nullable=True)
    dimension_2_code: Mapped[str] = mapped_column(String(20), nullable=True)
    blocked: Mapped[str] = mapped_column(String(20), nullable=True)
    priority: Mapped[int] = mapped_column(Integer, nullable=True)
