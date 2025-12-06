from typing import Annotated
from pydantic import BeforeValidator


def blank_str_to_none(value):
    if isinstance(value, str) and not value.strip():
        return None
    return value


BCString = Annotated[str | None, BeforeValidator(blank_str_to_none)]
