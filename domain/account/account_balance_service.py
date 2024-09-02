from abc import ABC, abstractmethod
from .models import AccountBalance


class AccountBalanceService(ABC):

    # TODO: get_balance(self, account_id: int)
    @abstractmethod
    async def get_balance(self, app_key: str, app_secret: str, account_number: str) -> AccountBalance:
        pass
