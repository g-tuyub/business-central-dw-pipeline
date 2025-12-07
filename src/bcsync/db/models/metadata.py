from sqlalchemy import MetaData
from bcsync.db.constants import NAMING_CONVENTION


metadata = MetaData(naming_convention=NAMING_CONVENTION)