from pydantic import BaseModel, ConfigDict, Field
from uuid import UUID
from datetime import datetime


class Base(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        frozen=True,
        extra='ignore'
    )


class BaseEntity(Base):
    system_id: UUID = Field(alias='systemId')
    system_created_at: datetime = Field(alias='systemCreatedAt')
    system_updated_at: datetime = Field(alias='systemUpdatedAt')
