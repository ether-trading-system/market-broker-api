import datetime
from typing import Optional

from common import RestClient

from core import settings, cache
from .dto import TokenPRequest, TokenPResponse
from .kis_exception import kis_error_handler


def get_ts(token: TokenPResponse) -> tuple[int, int]:
    expire_ts = int(datetime.datetime.strptime(token.access_token_token_expired, '%Y-%m-%d %H:%M:%S').timestamp())
    now_ts = int(datetime.datetime.now().timestamp())
    return expire_ts, now_ts


def expired(token: TokenPResponse) -> int:
    expire_ts, now_ts = get_ts(token)
    return now_ts - expire_ts > 0


def calc_ttl(token: TokenPResponse) -> int:
    expire_ts, now_ts = get_ts(token)
    return expire_ts - now_ts - 60


class KisAuthRest:
    _client = Optional[RestClient]

    async def __aenter__(self) -> "KisAuthRest":
        self._client = RestClient(
            headers={"Content-Type": "application/json"},
            base_url=settings.kis_base_url
        )
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self._client.close()

    @kis_error_handler
    async def issue_token(self, app_key: str, app_secret: str) -> TokenPResponse:
        async with self._client as client:
            body = TokenPRequest(
                grant_type='client_credentials',
                appkey=app_key,
                appsecret=app_secret
            )
            return await client.post('/oauth2/tokenP', body, TokenPResponse)

    async def get_token(self, app_key: str, app_secret: str) -> TokenPResponse:
        token = await cache.get_cache(key=app_key)
        if token is None or expired(token):
            token = await self.issue_token(app_key, app_secret)
            ttl = calc_ttl(token)
            await cache.set_cache(key=app_key, value=token, ttl=ttl)
        return token
