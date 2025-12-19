from bcsync.core.types import BCEntity, EntitySyncConfig
from bcsync.db.models import staging , core
from bcsync.api import schemas


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
    ),
    BCEntity.CUSTOMER_LEDGER_ENTRY: EntitySyncConfig(
        endpoint="customerLedgerEntries",
        validator_model=schemas.CustomerLedgerEntry,
        staging_model=staging.CustomerLedgerEntry,
        core_model=core.CustomerLedgerEntry,
    ),
    BCEntity.SALES_INVOICE_HEADER: EntitySyncConfig(
        endpoint="salesInvoices",
        validator_model=schemas.SalesInvoiceHeader,
        staging_model=staging.SalesInvoiceHeader,
        core_model=core.SalesInvoiceHeader,

    ),
    BCEntity.SALES_INVOICE_LINE: EntitySyncConfig(
        endpoint="salesInvoiceLines",
        validator_model=schemas.SalesInvoiceLine,
        staging_model=staging.SalesInvoiceLine,
        core_model=core.SalesInvoiceLine,
    )
}
