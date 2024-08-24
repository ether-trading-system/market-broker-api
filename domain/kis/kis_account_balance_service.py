from core import to_decimal
from domain.account import AccountBalanceService, AccountSecurityBalance, AccountBalance
from domain.kis.dto import KisBaseResponse, InquireBalanceResponse1, InquireBalanceResponse2
from domain.kis.kis_account_rest import KisAccountRest


class KisAccountBalanceService(AccountBalanceService):

    async def get_balance(self, app_key: str, app_secret: str, account_number: str):
        async with KisAccountRest() as kis_account_rest:
            balance_response = await kis_account_rest.get_balance(
                app_key=app_key, app_secret=app_secret,
                account_number=account_number
            )

            balance2: InquireBalanceResponse2 = balance_response.output2[0]

            return AccountBalance(
                deposit_received=to_decimal(balance2.dnca_tot_amt),
                deposit_received_d2=to_decimal(balance2.prvs_rcdl_excc_amt),
                total_evaluation_amount=to_decimal(balance2.tot_evlu_amt),
                securities=[*map(lambda x: AccountSecurityBalance(
                    ticker=x.pdno,
                    name=x.prdt_name,
                    holding_quantity=to_decimal(x.hldg_qty),
                    price=to_decimal(x.prpr),
                    average_buy_price=to_decimal(x.avg_buy_prpr),
                ), balance_response.output1)]
            )