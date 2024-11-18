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
    # 서비스 레이어에서 토큰을 가져오거나 갱신하도록 요청
    response = await AuthService.get_or_refresh_token(
        url_div=request.url_div, 
        api_key=request.api_key, 
        app_secret=request.app_secret, 
        access_token=request.access_token,
        expires_at=request.expires_at
    )
    
    # header와 data를 클라이언트에 반환
    if response["header"]["res_code"] != 200:
        raise HTTPException(status_code=response["header"]["res_code"], detail=response["data"])

    return response
