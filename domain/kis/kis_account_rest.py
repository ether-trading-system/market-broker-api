from dataclasses import asdict
from typing import Optional
from common import RestClient
from core import settings
from .dto import InquireBalanceRequestQuery, TokenPResponse, InquireBalanceResponse
from .kis_auth_rest import KisAuthRest
from .kis_exception import kis_error_handler


def get_tr_id(resource: str):
    tr_id_map = {
        'prod': {
            'inquire-balance': 'TTTC8434R'
        },
        'dev': {
            'inquire-balance': 'TTTC8434R'
        }
    }

    if settings.env == 'prod':
        return tr_id_map['prod'][resource]

    return tr_id_map['dev'][resource]


class KisAccountRest:
    _client = Optional[RestClient]

    async def __aenter__(self) -> "KisAccountRest":
        self._client = RestClient(
            base_url=settings.kis_base_url
        )
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self._client.close()

    @kis_error_handler
    async def get_balance(self, app_key: str, app_secret: str, account_number: str) -> InquireBalanceResponse:
        async with self._client as client:
            query = InquireBalanceRequestQuery(
                CANO=account_number[:8],
                ACNT_PRDT_CD='01',
                AFHR_FLPR_YN='N',
                OFL_YN='',
                INQR_DVSN='00',  # 전체
                UNPR_DVSN='01',  # 01 : 기본값
                FUND_STTL_ICLD_YN='Y',
                FNCG_AMT_AUTO_RDPT_YN='N',
                PRCS_DVSN='00',
                CTX_AREA_FK100='',
                CTX_AREA_NK100='',
            )

            async with KisAuthRest() as kis_auth_rest:
                token: TokenPResponse = await kis_auth_rest.get_token(app_key, app_secret)
                return await client.get(
                    '/uapi/domestic-stock/v1/trading/inquire-balance', InquireBalanceResponse,
                    headers={
                        'authorization': f'Bearer {token.access_token}',
                        'appkey': app_key,
                        'appsecret': app_secret,
                        'tr_id': get_tr_id('inquire-balance'),
                        'tr_cont': '',  # 연속 여부
                    },
                    params=asdict(query))
