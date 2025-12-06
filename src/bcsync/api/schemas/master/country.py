from bcsync.api.schemas.base import BCEntityModel
from bcsync.api.schemas.types import BCString


class Country(BCEntityModel):
    code: str
    name: BCString
