from fastapi import APIRouter
from pydantic import BaseModel

from domain.account.account_balance_factory import AccountProvider, AccountBalanceFactory

router = APIRouter()


class AccountBalanceRequest(BaseModel):
    app_key: str
    app_secret: str
    account_number: str


@router.get("/accounts", tags=["accounts"])
async def read_accounts():
    return [{"name": "Alice"}, {"name": "Bob"}]


@router.post("/accounts/balance", tags=["accounts"])
async def get_balance(body: AccountBalanceRequest):
    return await AccountBalanceFactory.find(AccountProvider.KIS).get_balance(
        app_key=body.app_key, app_secret=body.app_secret, account_number=body.account_number
    )
