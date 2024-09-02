from dataclasses import dataclass
from pydantic.dataclasses import dataclass as pdataclass


@dataclass
class TokenPRequest:
    """
    grant_type: "client_credentials"
    appkey: 한국투자증권 홈페이지에서 발급받은 appkey
    appsecret: 한국투자증권 홈페이지에서 발급받은 appsecret
    """
    grant_type: str
    appkey: str
    appsecret: str


@pdataclass
class TokenPResponse:
    """
    access_token: Access token 유효기간 1일
    token_type: 접근토큰유형 : "Bearer"
    expires_in: 유효기간(초)
    access_token_token_expired: 유효기간(년:월:일 시:분:초) "2022-08-30 08:10:10"
    """
    access_token: str
    token_type: str
    expires_in: int
    access_token_token_expired: str
