from sqlalchemy import String, Index
from sqlalchemy.orm import Mapped, mapped_column
from db.models.base import Base, SystemFieldsMixin


class PaymentTerm(Base, SystemFieldsMixin):
    __tablename__ = "payment_term"
    __table_args__ = (
        Index(None, "system_id", unique=True, mssql_clustered=True),
        {"schema": "staging"}
    )
    # Logical PK only, because staging tables are heap tables
    __mapper_args__ = {
        "primary_key": [SystemFieldsMixin.system_id]
    }

    code: Mapped[str] = mapped_column(String(10), nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=True)