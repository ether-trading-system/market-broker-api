import pytest

from http import HTTPStatus
from core import settings
from .kis_exception import KisException, KisErrorCode
from .kis_rest import KisRest


@pytest.mark.asyncio
async def test_get_token():
    async with KisRest() as rest:
        app_key = settings.kis_real_app_key
        app_secret = settings.kis_real_app_secret

        res = await rest.get_token(app_key, app_secret)

        assert res.access_token is not None


@pytest.mark.asyncio
async def test_get_token_with_kis_error():
    with pytest.raises(KisException) as error:
        async with KisRest() as rest:
            app_key = settings.kis_real_app_key
            app_secret = settings.kis_real_app_secret

            await rest.get_token(app_key, app_secret)
            await rest.get_token(app_key, app_secret)

    assert error.value.status_code == HTTPStatus.INTERNAL_SERVER_ERROR
    assert error.value.error_code == KisErrorCode.ACCESS_TOKEN_RATE_LIMIT_EXCEEDED.value
