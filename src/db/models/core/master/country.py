from sqlalchemy.orm import Mapped, mapped_column
from db.models.base import Base, SystemFieldsMixin, SurrogateKeyMixin
from sqlalchemy import String, Index


class Country(SurrogateKeyMixin, Base, SystemFieldsMixin):
    __tablename__ = 'country'
    __table_args__ = (
        Index(None, "system_id", unique=True, mssql_clustered=False),
        {
            "schema":"core"
        }
    )

    code: Mapped[str] = mapped_column(String(10), nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String(50), nullable=True)

