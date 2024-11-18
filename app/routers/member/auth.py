from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
from fastapi import APIRouter, HTTPException
from app.services.auth_service import AuthService

import logging
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
    """
    API Key와 App Secret으로 토큰을 가져오거나 갱신.
    표준화된 응답 구조:
    - header: 상태 코드
    - data: 토큰 정보 또는 에러 정보
    """
    try:
        # 서비스 레이어에서 토큰을 가져오거나 갱신하도록 요청
        response = await AuthService.get_or_refresh_token(
            url_div=request.url_div, 
            api_key=request.api_key, 
            app_secret=request.app_secret, 
            access_token=request.access_token,
            expires_at=request.expires_at
        )
        return response  # 성공과 실패 모두 표준 구조로 반환

    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")
        # 표준화된 실패 응답 반환
        return {
            "header": {"res_code": 500},
            "data": {"error_description": str(e), "error_code": "UNEXPECTED_ERROR"}
        }
