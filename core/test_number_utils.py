from decimal import Decimal

from core import to_decimal


def test_to_decimal_str():
    assert to_decimal('1.23') == Decimal('1.23')


def test_to_decimal_int():
    assert to_decimal(1) == Decimal('1')


def test_to_decimal_float():
    assert to_decimal(1.23) == Decimal('1.23')
