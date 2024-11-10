from fastapi import APIRouter
from app.exceptions.kis_exception import kis_error_handler
import httpx

router = APIRouter()

REQ_GET_KEY = "/oauth2/Approval"            # 실시간 접속키 발급
REQ_GET_HASH_KEY = "/uapi/hashkey"          # hash key 발급
REQ_GET_ACCESS_TOKEN = "/oauth2/tokenP"     # 접속토큰 발급
REQ_REMOVE_TOKEN = "/oauth2/revokeP"        # 접속토큰 폐기


@router.post("/get-token", tags=["auth"])
async def get_token(url: str, api_key: str, app_secret: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{url}{REQ_GET_ACCESS_TOKEN}", json={
            "grant_type": "client_credentials",     # 고정
            "appkey": api_key,
            "appsecret": app_secret,
        })
        
        return response.json()