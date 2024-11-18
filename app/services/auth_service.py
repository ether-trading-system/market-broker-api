from app.clients.kis_client import KISClient
from datetime import datetime, timedelta
import logging

class AuthService:
    @staticmethod
    async def get_or_refresh_token(url_div: str, api_key: str, app_secret: str, access_token: str, expires_at: datetime) -> dict:
        """토큰 만료 시간을 확인 -> 갱신할여부를 판단 & 처리"""
        if not access_token or not expires_at or expires_at < datetime.now():
            logging.info("[get_or_refresh_token] 토큰이 만료되었습니다. 토큰을 갱신합니다.")
            token_info = await KISClient.get_access_token(url_div, api_key, app_secret)
            access_token = token_info["access_token"]
            expires_in = token_info["expires_in"]
            access_token_token_expired = token_info["access_token_token_expired"]
        
        return {
            "access_token": access_token,
            "expires_in": expires_in,
            "token_type": "Bearer",      # 고정
            "access_token_token_expired": access_token_token_expired
        }