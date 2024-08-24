from enum import Enum
from http import HTTPStatus
from dataclasses import dataclass
from core import EtherException, EtherRestClientException


class KisErrorCode(Enum):
    ACCESS_TOKEN_RATE_LIMIT_EXCEEDED = 'ACCESS_TOKEN_RATE_LIMIT_EXCEEDED'
    INVALID_APP_KEY_OR_SECRET = 'INVALID_APP_KEY_OR_SECRET'
    UNKNOWN = 'UNKNOWN'


error_map = {
    # {'error_code': 'EGW00133', 'error_description': '접근토큰 발급 잠시 후 다시 시도하세요(1분당 1회)'}
    'EGW00133': KisErrorCode.ACCESS_TOKEN_RATE_LIMIT_EXCEEDED,
    # {'error_code': 'EGW00002', 'error_description': '서버 에러가 발생했습니다.'}
    'EGW00002': KisErrorCode.INVALID_APP_KEY_OR_SECRET
}


@dataclass
class KisError:
    error_code: str
    error_description: str


class KisException(EtherException):

    def __init__(self, response: EtherRestClientException):
        kis_error = KisError(**response.response_body)
        error_code = error_map.get(kis_error.error_code, KisErrorCode.UNKNOWN)

        status_code = HTTPStatus.INTERNAL_SERVER_ERROR
        match response.status_code:
            case 400:
                status_code = HTTPStatus.BAD_REQUEST

        super().__init__(
            error=response,
            error_code=error_code.value,
            status_code=status_code,
            message=f'[kis_error] {error_code.value}',
            detail=f'[kis_error] {kis_error.error_code} - {kis_error.error_description}',
            data=response.response_body
        )


def kis_error_handler(func):
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except EtherRestClientException as e:
            raise KisException(e)

    return wrapper
