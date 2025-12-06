from pydantic import BaseModel, ConfigDict, Field, BeforeValidator
from uuid import UUID
from datetime import datetime


class Base(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        frozen=True,
        extra='ignore'
    )


class BCEntityModel(Base):
    system_id: UUID = Field(alias='systemId')
    company_id: UUID = Field(alias='companyId')
    system_created_at: datetime = Field(alias='systemCreatedAt')
    system_modified_at: datetime = Field(alias='systemModifiedAt')
    system_created_by_id: UUID = Field(alias='systemCreatedBy')
    system_modified_by_id: UUID = Field(alias='systemModifiedBy')
