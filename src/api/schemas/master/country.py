from api.schemas.base import BaseEntity


class Country(BaseEntity):
    code: str
    name: str
