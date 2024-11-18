import httpx
import logging
from app.exceptions.kis_response_handler import HTTPResponseHandler

class KISClient:
    BASE_URL_SIMULATE = "https://openapivts.koreainvestment.com:29443"
    BASE_URL_REAL = "https://openapivts.koreainvestment.com:29443"

    @staticmethod
    async def get_access_token(url_div: str, api_key: str, app_secret: str) -> dict:
        """한투 API에 토큰 요청을 보내고 응답을 반환"""

        # div_url에 따라 BASE_URL 설정
        if url_div == "simulate":
            base_url = KISClient.BASE_URL_SIMULATE
        else:
            base_url = KISClient.BASE_URL_REAL

        logging.info(f"[CLIENTS] base_url : {base_url}")
        url = f"{base_url}/oauth2/tokenP"
        payload = {
            "grant_type": "client_credentials",
            "appkey": api_key,
            "appsecret": app_secret
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=payload)
            # response.raise_for_status()  # 상태 코드가 200이 아니면 예외 발생
            # return response.json()
            return HTTPResponseHandler.parse_response(response)
