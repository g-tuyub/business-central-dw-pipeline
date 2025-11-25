from sqlalchemy import String, Float, Boolean, Index
from sqlalchemy.orm import Mapped, mapped_column
from db.models.base import Base, SystemFieldsMixin


class Item(Base, SystemFieldsMixin):
    __tablename__ = "item"

    __table_args__ = (
        Index(None, "system_id", unique=True, mssql_clustered=True),
        {"schema": "staging"}
    )
    __mapper_args__ = {"primary_key": [SystemFieldsMixin.system_id]}

    code: Mapped[str] = mapped_column(String(20), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=True)
    name_2: Mapped[str] = mapped_column(String(100), nullable=True)
    bar_code: Mapped[str] = mapped_column(String(20), nullable=True)
    item_type: Mapped[str] = mapped_column(String(20), nullable=True)
    item_category_code: Mapped[str] = mapped_column(String(20), nullable=True)
    inventory_posting_group_code: Mapped[str] = mapped_column(String(20), nullable=True)
    country_of_origin_code: Mapped[str] = mapped_column(String(10), nullable=True)
    base_unit_of_measure_code: Mapped[str] = mapped_column(String(10), nullable=True)
    dimension_1_code: Mapped[str] = mapped_column(String(20), nullable=True)
    dimension_2_code: Mapped[str] = mapped_column(String(20), nullable=True)
    unit_price: Mapped[float] = mapped_column(Float, nullable=True)
    unit_cost: Mapped[float] = mapped_column(Float, nullable=True)
    standard_cost: Mapped[float] = mapped_column(Float, nullable=True)
    unit_list_price: Mapped[float] = mapped_column(Float, nullable=True)
    profit_percentage: Mapped[float] = mapped_column(Float, nullable=True)
    gross_weight: Mapped[float] = mapped_column(Float, nullable=True)
    net_weight: Mapped[float] = mapped_column(Float, nullable=True)
    safety_stock_quantity: Mapped[float] = mapped_column(Float, nullable=True)
    costing_method: Mapped[str] = mapped_column(String(20), nullable=True)
    price_profit_calculation: Mapped[str] = mapped_column(String(20), nullable=True)
    assembly_policy: Mapped[str] = mapped_column(String(20), nullable=True)
    manufacturing_policy: Mapped[str] = mapped_column(String(20), nullable=True)
    stockout_warning: Mapped[str] = mapped_column(String(20), nullable=True)
    reserve: Mapped[str] = mapped_column(String(20), nullable=True)
    price_includes_vat: Mapped[bool] = mapped_column(Boolean, nullable=True)
    blocked: Mapped[bool] = mapped_column(Boolean, nullable=True)
    sales_blocked: Mapped[bool] = mapped_column(Boolean, nullable=True)
    purchasing_blocked: Mapped[bool] = mapped_column(Boolean, nullable=True)
    service_blocked: Mapped[bool] = mapped_column(Boolean, nullable=True)
    critical: Mapped[bool] = mapped_column(Boolean, nullable=True)