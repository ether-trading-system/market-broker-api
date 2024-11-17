from app.clients.kis_client import KISClient
from datetime import datetime, timedelta

class AuthService:
    @staticmethod
    async def get_or_refresh_token(api_key: str, app_secret: str, db_user) -> dict:
        """토큰 만료 시간을 확인 -> 갱신할여부를 판단 & 처리"""
        if db_user.access_token_expires < datetime.now():
            # 토큰이 만료되었으므로 갱신
            token_info = await KISClient.get_access_token(api_key, app_secret)
            db_user.access_token = token_info["access_token"]
            db_user.token_type = token_info["token_type"]
            db_user.expires_in = token_info["expires_in"]
            db_user.access_token_expires = datetime.now() + timedelta(seconds=db_user.expires_in)
            # DB에 갱신된 토큰 정보 저장 로직 추가 필요
        return {
            "access_token": db_user.access_token,
            "expires_in": db_user.expires_in,
            "token_type": db_user.token_type,
        }