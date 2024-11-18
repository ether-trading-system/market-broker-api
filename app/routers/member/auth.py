from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from app.services.auth_service import AuthService

import httpx

router = APIRouter()

REQ_GET_KEY = "/oauth2/Approval"            # 실시간 접속키 발급
REQ_GET_HASH_KEY = "/uapi/hashkey"          # hash key 발급
REQ_GET_ACCESS_TOKEN = "/oauth2/tokenP"     # 접속토큰 발급
REQ_REMOVE_TOKEN = "/oauth2/revokeP"        # 접속토큰 폐기




class TokenRequest(BaseModel):
    url_div: str
    api_key: str
    app_secret: str
    access_token: str = None
    expires_at: datetime = None


@router.post("/get-token", tags=["auth"])
async def get_token(request: TokenRequest):
    """API Key와 app secret으로 토큰을 가져오거나 갱신"""
    try:
        # 서비스 레이어에서 토큰을 가져오거나 갱신하도록 요청
        token_info = await AuthService.get_or_refresh_token(
            request.url_div, 
            request.api_key, 
            request.app_secret, 
            request.access_token,
            request.expires_at
        )
        print(token_info)

        return token_info
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
