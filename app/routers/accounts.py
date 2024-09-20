from fastapi import APIRouter
from pydantic import BaseModel

from app.crud.accounts import save_accounts
from core.deps import SessionDep
from domain.account.account_balance_factory import AccountProvider, AccountBalanceFactory

router = APIRouter()


class AccountBalanceRequest(BaseModel):
    app_key: str
    app_secret: str
    account_number: str


class AccountCreateRequest(BaseModel):
    api_key: str
    access_token: str
    account_number: str
    product_id: str


@router.get("/accounts", tags=["accounts"])
async def read_accounts():
    return [{"name": "Alice"}, {"name": "Bob"}]


@router.post("/accounts/balance", tags=["accounts"])
async def get_balance(body: AccountBalanceRequest):
    return await AccountBalanceFactory.find(AccountProvider.KIS).get_balance(
        app_key=body.app_key, app_secret=body.app_secret, account_number=body.account_number
    )


@router.post("/accounts", tags=["accounts"])
async def create_account(body: AccountCreateRequest, db: SessionDep):
    return save_accounts(db=db, account_number=body.account_number, api_key=body.api_key,
                         access_token=body.access_token, product_id=body.product_id)
