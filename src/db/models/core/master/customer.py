from sqlalchemy import String, Float, Integer, Boolean, Index, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from db.models.base import Base, SystemFieldsMixin, SurrogateKeyMixin


class Customer(SurrogateKeyMixin, Base, SystemFieldsMixin):
    __tablename__ = "customer"
    __table_args__ = (
        Index(None, "system_id", unique=True, mssql_clustered=False),
        {"schema": "core"}
    )

    code: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String(100), nullable=True)
    customer_posting_group_id: Mapped[int] = mapped_column(Integer, ForeignKey("core.customer_posting_group.id"),nullable=True)
    customer_price_group_id: Mapped[int] = mapped_column(Integer, ForeignKey("core.customer_price_group.id"),nullable=True)
    currency_id: Mapped[int] = mapped_column(Integer, ForeignKey("core.currency.id"), nullable=True)
    payment_term_id: Mapped[int] = mapped_column(Integer, ForeignKey("core.payment_term.id"), nullable=True)
    payment_method_id: Mapped[int] = mapped_column(Integer, ForeignKey("core.payment_method.id"), nullable=True)
    salesperson_id: Mapped[int] = mapped_column(Integer, ForeignKey("core.salesperson.id"), nullable=True)
    shipment_method_id: Mapped[int] = mapped_column(Integer, ForeignKey("core.shipment_method.id"), nullable=True)
    location_id: Mapped[int] = mapped_column(Integer, ForeignKey("core.location.id"), nullable=True)
    country_id: Mapped[int] = mapped_column(Integer, ForeignKey("core.country.id"), nullable=True)
    address_line_1: Mapped[str] = mapped_column(String(100), nullable=True)
    address_line_2: Mapped[str] = mapped_column(String(50), nullable=True)
    postal_code: Mapped[str] = mapped_column(String(20), nullable=True)
    ship_to_address_code: Mapped[str] = mapped_column(String(20), nullable=True)
    credit_limit: Mapped[float] = mapped_column(Float, nullable=True)
    combine_shipments: Mapped[bool] = mapped_column(Boolean, nullable=True)
    dimension_1_code: Mapped[str] = mapped_column(String(20), nullable=True)
    dimension_2_code: Mapped[str] = mapped_column(String(20), nullable=True)
    blocked: Mapped[str] = mapped_column(String(20), nullable=True)
    priority: Mapped[int] = mapped_column(Integer, nullable=True)

