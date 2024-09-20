from datetime import datetime

from app.decorators.transaction_decorators import transactional
from app.models.account import Account
from core.deps import SessionDep


@transactional()
def save_accounts(db: SessionDep, account_number: str, api_key: str, access_token: str, product_id: str):
    account = Account(
        account_number=account_number,
        api_key=api_key,
        access_token=access_token,
        product_id=product_id,
        cr_dt=datetime.now()
    )
    db.add(account)
    return account
