from fastapi import APIRouter
from app.exceptions.kis_exception import kis_error_handler
from core.config_manager import config_manager
from core.settings import get_kis_api_info
import httpx

router = APIRouter()

REQ_GET_KEY = "/oauth2/Approval"            # 실시간 접속키 발급
REQ_GET_HASH_KEY = "/uapi/hashkey"          # hash key 발급
REQ_GET_ACCESS_TOKEN = "/oauth2/tokenP"     # 접속토큰 발급
REQ_REMOVE_TOKEN = "/oauth2/revokeP"        # 접속토큰 폐기


@router.post("/get-token", tags=["auth"])
async def get_token(url_kind: str):
    config_manager.set("url_kind", url_kind)  # "simulate" 또는 "real"
    
    base_url = config_manager.get_base_url()
    api_key = config_manager.get("KIS_APP_KEY")
    app_secret = config_manager.get("KIS_APP_SECRET")
    
    print(get_kis_api_info())
    
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{base_url}{REQ_GET_ACCESS_TOKEN}", json={
            "grant_type": "client_credentials",  # 고정 값
            "appkey": api_key,
            "appsecret": app_secret,
        })
        
        return response.json()