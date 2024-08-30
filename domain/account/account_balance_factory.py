from domain.account.constants import AccountProvider
from domain.kis import KisAccountBalanceService

balanceMap = {
    AccountProvider.KIS: KisAccountBalanceService()
}

assert len(balanceMap) == len(AccountProvider)


class AccountBalanceFactory:

    @staticmethod
    def find(provider: AccountProvider):
        match provider:
            case AccountProvider.KIS:
                return balanceMap[provider]
            case _:
                raise ValueError('Invalid provider')
