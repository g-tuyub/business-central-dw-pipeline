from typing import Annotated, Any
from decimal import Decimal, ROUND_HALF_UP
from pydantic import BeforeValidator


def blank_str_to_none(value):
    if isinstance(value, str) and not value.strip():
        return None
    return value


BCString = Annotated[str | None, BeforeValidator(blank_str_to_none)]


def normalize_decimal(value):
    if value is None or value == "":
        return None
    d = Decimal(str(value))
    return d.quantize(Decimal("0.00001"), rounding=ROUND_HALF_UP)

BCDecimal = Annotated[Decimal | None, BeforeValidator(normalize_decimal)]