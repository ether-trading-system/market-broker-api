from typing import Optional
from core import settings, RestClient
from .dto import TokenPRequest, TokenPResponse
from .kis_exception import kis_error_handler


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
    async def get_token(self, app_key: str, app_secret: str) -> TokenPResponse:
        async with self._client as client:
            body = TokenPRequest(
                grant_type='client_credentials',
                appkey=app_key,
                appsecret=app_secret
            )

            return await client.post('/oauth2/tokenP', body, TokenPResponse)
