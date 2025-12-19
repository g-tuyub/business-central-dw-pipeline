from enum import StrEnum
from typing import Literal, Optional, Type
from pydantic import BaseModel
from dataclasses import dataclass
from bcsync.db.models.base import CoreBase, StagingBase
from bcsync.api.schemas.base import BCEntityBase

class SyncMetrics(BaseModel):
    table: str
    endpoint: str
    rows_extracted: int = 0
    rows_inserted: int = 0
    rows_updated: int = 0
    rows_fixed: int = 0
    time_elapsed: float = 0.0
    state: Literal['SUCCESS','FAILURE','PENDING'] = 'PENDING'


class BCEntity(StrEnum):
    """
    Catálogo de entidades de Business Central disponibles para sincronizar.
    """
    COUNTRY = "country"
    CURRENCY = "currency"
    CUSTOMER = "customer"
    CUSTOMER_POSTING_GROUP = "customer_posting_group"
    CUSTOMER_PRICE_GROUP = "customer_price_group"
    EXCHANGE_RATE = "exchange_rate"
    INVENTORY_POSTING_GROUP = "inventory_posting_group"
    ITEM = "item"
    ITEM_CATEGORY = "item_category"
    LOCATION = "location"
    PAYMENT_METHOD = "payment_method"
    PAYMENT_TERM = "payment_term"
    SALESPERSON = "salesperson"
    SHIP_TO_ADDRESS = "ship_to_address"
    SHIPMENT_METHOD = "shipment_method"
    VENDOR = "vendor"
    VENDOR_POSTING_GROUP = "vendor_posting_group"
    CUSTOMER_LEDGER_ENTRY = "customer_ledger_entry"
    SALES_INVOICE_HEADER = "sales_invoice_header"
    SALES_INVOICE_LINE = "sales_invoice_line"


@dataclass(frozen=True)
class EntitySyncConfig:
    endpoint: str
    validator_model: Type[BCEntityBase]
    staging_model: Type[StagingBase]
    core_model: Type[CoreBase]
    requires_fixer : bool = False

    @property
    def staging_table(self) -> str:
        return self.staging_model.__tablename__

    @property
    def staging_schema(self) -> str:
        return self.staging_model.__table__.schema

    @property
    def core_table(self) -> str:
        return self.core_model.__tablename__

    @property
    def core_schema(self) -> str:
        return self.core_model.__table__.schema

    @property
    def loader_procedure(self) -> str:
        return f'{self.core_schema}.sp_load_{self.core_table}'

    @property
    def fixer_procedure(self) -> Optional[str]:
        if self.requires_fixer:
            return f'{self.core_schema}.sp_fix_{self.core_table}_references'
        return None