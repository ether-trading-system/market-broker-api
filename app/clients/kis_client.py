import httpx

class KISClient:
    BASE_URL = "https://openapivts.koreainvestment.com:29443"

    @staticmethod
    async def get_access_token(api_key: str, app_secret: str) -> dict:
        """한투 API에 토큰 요청을 보내고 응답을 반환"""
        url = f"{KISClient.BASE_URL}/oauth2/tokenP"
        payload = {
            "grant_type": "client_credentials",
            "appkey": api_key,
            "appsecret": app_secret
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=payload)
            response.raise_for_status()  # 상태 코드가 200이 아니면 예외 발생
            return response.json()
