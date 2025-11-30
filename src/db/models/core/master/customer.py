from sqlalchemy import String, Float, Integer, Boolean, Index, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from db.models.base import CoreBase


class Customer(CoreBase):
    __tablename__ = "customer"
    __additional_indexes__ = (
        Index(None, "code", unique=True),
    )

    code: Mapped[str] = mapped_column(String(20), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=True)
    customer_posting_group_id: Mapped[int] = mapped_column(Integer, nullable=True, index=True)
    customer_posting_group_code: Mapped[str] = mapped_column(String(20), nullable=True)
    customer_price_group_id: Mapped[int] = mapped_column(Integer, nullable=True, index=True)
    customer_price_group_code: Mapped[str] = mapped_column(String(20), nullable=True)
    currency_id: Mapped[int] = mapped_column(Integer, nullable=True, index=True)
    currency_code: Mapped[str] = mapped_column(String(10), nullable=True)
    payment_term_id: Mapped[int] = mapped_column(Integer, nullable=True, index=True)
    payment_term_code: Mapped[str] = mapped_column(String(20), nullable=True)
    payment_method_id: Mapped[int] = mapped_column(Integer, nullable=True, index=True)
    payment_method_code: Mapped[str] = mapped_column(String(20), nullable=True)
    salesperson_id: Mapped[int] = mapped_column(Integer, nullable=True, index=True)
    salesperson_code: Mapped[str] = mapped_column(String(20), nullable=True)
    shipment_method_id: Mapped[int] = mapped_column(Integer, nullable=True, index=True)
    shipment_method_code: Mapped[str] = mapped_column(String(20), nullable=True)
    location_id: Mapped[int] = mapped_column(Integer, nullable=True, index=True)
    location_code: Mapped[str] = mapped_column(String(20), nullable=True)
    address_line_1: Mapped[str] = mapped_column(String(100), nullable=True)
    address_line_2: Mapped[str] = mapped_column(String(50), nullable=True)
    postal_code: Mapped[str] = mapped_column(String(20), nullable=True)
    ship_to_address_code: Mapped[str] = mapped_column(String(20), nullable=True)
    country_id: Mapped[int] = mapped_column(Integer, nullable=True, index=True)
    country_code: Mapped[str] = mapped_column(String(10), nullable=True)
    credit_limit: Mapped[float] = mapped_column(Float, nullable=True)
    combine_shipments: Mapped[bool] = mapped_column(Boolean, nullable=True)
    dimension_1_code: Mapped[str] = mapped_column(String(20), nullable=True)
    dimension_2_code: Mapped[str] = mapped_column(String(20), nullable=True)
    blocked: Mapped[str] = mapped_column(String(20), nullable=True)
    priority: Mapped[int] = mapped_column(Integer, nullable=True)

