from dataclasses import dataclass
from pydantic.dataclasses import dataclass as pdataclass


@dataclass
class ApprovalRequest:
    """
        grant_type: "client_credentials"
        appkey: 한국투자증권 홈페이지에서 발급받은 appkey
        appsecret: 한국투자증권 홈페이지에서 발급받은 appsecret
        """
    grant_type: str
    appkey: str
    secretkey: str


@pdataclass
class ApprovalResponse:
    """웹소켓 이용 시 발급받은 웹소켓 접속키를 appkey와 appsecret 대신 헤더에 넣어 API 호출합니다."""
    approval_key: str
