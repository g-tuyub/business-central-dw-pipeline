from pydantic import BaseModel, ConfigDict, Field
from uuid import UUID
from datetime import datetime


class Base(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        frozen=True,
        extra='ignore'
    )


class BCEntityBase(Base):
    """
    Clase base abstracta para todos los esquemas de validación de la API de BC.

    Cualquier modelo que herede de esta clase representa la estructura de un objeto JSON
    tal como viene de la API OData de Business Central.
    """
    system_id: UUID = Field(alias='systemId')
    company_id: UUID = Field(alias='companyId')
    system_created_at: datetime = Field(alias='systemCreatedAt')
    system_modified_at: datetime = Field(alias='systemModifiedAt')
    system_created_by_id: UUID = Field(alias='systemCreatedBy')
    system_modified_by_id: UUID = Field(alias='systemModifiedBy')
