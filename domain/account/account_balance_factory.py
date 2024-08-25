from enum import Enum

from domain.kis import KisAccountBalanceService


class AccountProvider(Enum):
    KIS = 'kis'


balanceMap = {
    AccountProvider.KIS: KisAccountBalanceService()
}


class AccountBalanceFactory:

    @staticmethod
    def find(provider: AccountProvider):
        match provider:
            case AccountProvider.KIS:
                return balanceMap[provider]
            case _:
                raise ValueError('Invalid provider')


