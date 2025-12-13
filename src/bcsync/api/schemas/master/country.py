from bcsync.api.schemas.base import BCEntityBase
from bcsync.api.schemas.types import BCString


class Country(BCEntityBase):
    code: str
    name: BCString
