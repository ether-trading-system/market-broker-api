from app.clients.kis_client import KISClient
from datetime import datetime, timedelta
import logging

class AuthService:
    @staticmethod
    async def get_or_refresh_token(url_div: str, api_key: str, app_secret: str, access_token: str, expires_at: datetime) -> dict:
        try:
            """토큰 만료 시간을 확인(만료기간이 6시간 내로 남았을 때) -> 갱신할여부를 판단 & 처리"""
            if not access_token or not expires_at or expires_at < datetime.now() + timedelta(hours=6):
                logging.info("[get_or_refresh_token] 토큰이 만료되었습니다. 토큰을 갱신합니다.")
                return await KISClient.get_access_token(url_div, api_key, app_secret)

            logging.info("[get_or_refresh_token] 유효한 토큰이 존재합니다.")
            # 유효한 토큰 정보 반환
            return {
                "header": {"res_code": 200},
                "data": {
                    "access_token": access_token,
                    "expires_at": expires_at,
                    "token_type": "Bearer"
                }
            }
        except Exception as e:
            logging.error(f"토큰 갱신 중 오류 발생: {e}")
            # 예외 발생 시 응답
            return {
                "header": {"res_code": 500},
                "data": {"error_description": str(e), "error_code": "TOKEN_REFRESH_ERROR"}
            }