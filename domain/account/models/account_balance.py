from dataclasses import dataclass
from decimal import Decimal
from typing import List


@dataclass
class AccountSecurityBalance:
    ticker: str
    """종목코드"""

    name: str
    """종목명"""

    holding_quantity: Decimal
    """보유수량"""

    price: Decimal
    """현재가"""

    average_buy_price: Decimal
    """매입평균가"""


@dataclass
class AccountBalance:
    deposit_received: Decimal
    """예수금"""

    deposit_received_d2: Decimal
    """D+2 예수금"""

    total_evaluation_amount: Decimal
    """총평가금액"""

    securities: List[AccountSecurityBalance]
    """종목별 보유수량"""
