from decimal import Decimal

import pytest

from core import to_decimal


def test_to_decimal_str():
    assert to_decimal('1.23') == Decimal('1.23')


def test_to_decimal_int():
    assert to_decimal(1) == Decimal('1')


def test_to_decimal_float():
    assert to_decimal(1.23) == Decimal('1.23')


def test_to_wrong_str():
    with pytest.raises(ValueError) as e:
        to_decimal('a')

    # contains
    assert 'Could not convert' in str(e.value)
