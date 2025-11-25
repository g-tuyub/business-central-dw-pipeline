from sqlalchemy.orm import Mapped, mapped_column
from db.models.base import Base, SystemFieldsMixin
from sqlalchemy import String, Index


class Country(Base, SystemFieldsMixin):
    __tablename__ = 'country'
    __table_args__ = (
        Index(None, "system_id", unique=True, mssql_clustered=True),
        {
            "schema": "staging",
        }
    )
    __mapper_args__ = {
       "primary_key": [SystemFieldsMixin.system_id]
    }

    code : Mapped[String] = mapped_column(String(10),nullable=False)
    name : Mapped[String] = mapped_column(String(50),nullable=True)
