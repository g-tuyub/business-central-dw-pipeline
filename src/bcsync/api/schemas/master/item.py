from typing import Optional
from pydantic import Field
from bcsync.api.schemas.base import BCEntityModel
from bcsync.api.schemas.types import BCString


class Item(BCEntityModel):
    code: str = Field(alias='no')
    name: BCString = Field(alias='description')
    name_2: BCString = Field(alias='description2')
    bar_code: BCString = Field(alias='gtin')
    item_type: BCString = Field(alias='type')
    item_category_code: BCString = Field(alias='itemCategoryCode')
    inventory_posting_group_code: BCString = Field(alias='inventoryPostingGroup')
    country_of_origin_code: BCString = Field(alias='countryOfOriginCode')
    base_unit_of_measure_code: BCString = Field(alias='baseUnitOfMeasure')
    dimension_1_code: BCString = Field(alias='globalDimension1Code')
    dimension_2_code: BCString = Field(alias='globalDimension2Code')
    unit_price: float = Field(alias='unitPrice')
    unit_cost: float = Field(alias='unitCost')
    standard_cost: float = Field(alias='standardCost')
    unit_list_price: float = Field(alias='unitListPrice')
    profit_percentage: float = Field(alias='profitPercentage')
    price_includes_vat: bool = Field(alias='priceIncludesVAT')
    costing_method: BCString = Field(alias='costingMethod')
    price_profit_calculation: BCString = Field(alias='priceProfitCalculation')
    gross_weight: float = Field(alias='grossWeight')
    net_weight: float = Field(alias='netWeight')
    safety_stock_quantity: float = Field(alias='safetyStockQuantity')
    assembly_policy: BCString = Field(alias='assemblyPolicy')
    manufacturing_policy: BCString = Field(alias='manufacturingPolicy')
    stockout_warning: BCString = Field(alias='stockoutWarning')
    reserve: BCString = Field(alias='reserve')
    blocked: bool = Field(alias='blocked')
    sales_blocked: bool = Field(alias='salesBlocked')
    purchasing_blocked: bool = Field(alias='purchasingBlocked')
    service_blocked: bool = Field(alias='serviceBlocked')
    critical: bool = Field(alias='critical')
