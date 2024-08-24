from decimal import Decimal
from typing import Union


def to_decimal(value: Union[str, int, float]) -> Decimal:
    return Decimal(str(value))
