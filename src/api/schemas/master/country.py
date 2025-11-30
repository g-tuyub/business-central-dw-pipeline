from api.schemas.base import BCEntityModel


class Country(BCEntityModel):
    code: str
    name: str
