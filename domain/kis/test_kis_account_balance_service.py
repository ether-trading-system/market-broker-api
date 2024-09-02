import pytest

from .kis_account_balance_service import KisAccountBalanceService


@pytest.mark.skip
@pytest.mark.asyncio
async def test_get_balance():
    service = KisAccountBalanceService()

    balance = await service.get_balance(
        app_key='',
        app_secret='',
        account_number=''
    )

    print(balance)
