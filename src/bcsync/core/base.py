import logging
from dataclasses import dataclass
from typing import Type
from enum import StrEnum
from bcsync.db.models.base import StagingBase, CoreBase
from bcsync.api.schemas.base import BCEntityModel
from bcsync.api import schemas
from bcsync.db.models import staging
from bcsync.db.models import core

logger = logging.getLogger(__name__)


class BCEntity(StrEnum):
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


@dataclass(frozen=True)
class EntitySyncConfig:
    endpoint: str
    validator_model: Type[BCEntityModel]
    staging_model: Type[StagingBase]
    core_model: Type[CoreBase]

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
    def loader_sp(self):
        return f"{self.core_schema}.sp_load_{self.core_table}"


SYNC_TARGETS = {
    BCEntity.COUNTRY: EntitySyncConfig(
        endpoint="countries",
        validator_model=schemas.Country,
        staging_model=staging.Country,
        core_model=core.Country,
    ),
    BCEntity.CURRENCY: EntitySyncConfig(
        endpoint="currencies",
        validator_model=schemas.Currency,
        staging_model=staging.Currency,
        core_model=core.Currency,
    ),
    BCEntity.CUSTOMER: EntitySyncConfig(
        endpoint="customers",
        validator_model=schemas.Customer,
        staging_model=staging.Customer,
        core_model=core.Customer,
    ),
    BCEntity.CUSTOMER_POSTING_GROUP: EntitySyncConfig(
        endpoint="customerPostingGroups",
        validator_model=schemas.CustomerPostingGroup,
        staging_model=staging.CustomerPostingGroup,
        core_model=core.CustomerPostingGroup,
    ),
    BCEntity.CUSTOMER_PRICE_GROUP: EntitySyncConfig(
        endpoint="customerPriceGroups",
        validator_model=schemas.CustomerPriceGroup,
        staging_model=staging.CustomerPriceGroup,
        core_model=core.CustomerPriceGroup,
    ),
    BCEntity.EXCHANGE_RATE: EntitySyncConfig(
        endpoint="exchangeRates",
        validator_model=schemas.ExchangeRate,
        staging_model=staging.ExchangeRate,
        core_model=core.ExchangeRate,
    ),
    BCEntity.INVENTORY_POSTING_GROUP: EntitySyncConfig(
        endpoint="inventoryPostingGroups",
        validator_model=schemas.InventoryPostingGroup,
        staging_model=staging.InventoryPostingGroup,
        core_model=core.InventoryPostingGroup,
    ),
    BCEntity.ITEM: EntitySyncConfig(
        endpoint="items",
        validator_model=schemas.Item,
        staging_model=staging.Item,
        core_model=core.Item,
    ),
    BCEntity.ITEM_CATEGORY: EntitySyncConfig(
        endpoint="itemCategories",
        validator_model=schemas.ItemCategory,
        staging_model=staging.ItemCategory,
        core_model=core.ItemCategory,
    ),
    BCEntity.LOCATION: EntitySyncConfig(
        endpoint="locations",
        validator_model=schemas.Location,
        staging_model=staging.Location,
        core_model=core.Location,
    ),
    BCEntity.PAYMENT_METHOD: EntitySyncConfig(
        endpoint="paymentMethods",
        validator_model=schemas.PaymentMethod,
        staging_model=staging.PaymentMethod,
        core_model=core.PaymentMethod,
    ),
    BCEntity.PAYMENT_TERM: EntitySyncConfig(
        endpoint="paymentTerms",
        validator_model=schemas.PaymentTerm,
        staging_model=staging.PaymentTerm,
        core_model=core.PaymentTerm,
    ),
    BCEntity.SALESPERSON: EntitySyncConfig(
        endpoint="salesPersons",
        validator_model=schemas.Salesperson,
        staging_model=staging.Salesperson,
        core_model=core.Salesperson,
    ),
    BCEntity.SHIP_TO_ADDRESS: EntitySyncConfig(
        endpoint="shipToAddresses",
        validator_model=schemas.ShipToAddress,
        staging_model=staging.ShipToAddress,
        core_model=core.ShipToAddress,
    ),
    BCEntity.SHIPMENT_METHOD: EntitySyncConfig(
        endpoint="shipmentMethods",
        validator_model=schemas.ShipmentMethod,
        staging_model=staging.ShipmentMethod,
        core_model=core.ShipmentMethod,
    ),
    BCEntity.VENDOR: EntitySyncConfig(
        endpoint="vendors",
        validator_model=schemas.Vendor,
        staging_model=staging.Vendor,
        core_model=core.Vendor,
    ),
    BCEntity.VENDOR_POSTING_GROUP: EntitySyncConfig(
        endpoint="vendorPostingGroups",
        validator_model=schemas.VendorPostingGroup,
        staging_model=staging.VendorPostingGroup,
        core_model=core.VendorPostingGroup,
    )
}


class RegistryIntegrityError(Exception):
    pass


def _validate_registry() -> None:
    defined_entities = set(BCEntity)
    defined_configurations = set(SYNC_TARGETS.keys())
    missing = defined_entities - defined_configurations

    if missing:
        error_message = f"The following entities : {missing} are defined in the Enum but are missing configuration in SYNC_TARGETS"
        logger.critical(error_message)
        raise RegistryIntegrityError(error_message)


_validate_registry()
