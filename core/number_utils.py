from decimal import Decimal, InvalidOperation
from typing import Union


def to_decimal(value: Union[str, int, float]) -> Decimal:
    try:
        return Decimal(str(value))
    except (ValueError, InvalidOperation) as e:
        raise ValueError(f"Could not convert '{value}' to Decimal: {e}")

