from fastapi import APIRouter
from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException
from app.services.auth_service import AuthService

import httpx

router = APIRouter()

REQ_GET_KEY = "/oauth2/Approval"            # 실시간 접속키 발급
REQ_GET_HASH_KEY = "/uapi/hashkey"          # hash key 발급
REQ_GET_ACCESS_TOKEN = "/oauth2/tokenP"     # 접속토큰 발급
REQ_REMOVE_TOKEN = "/oauth2/revokeP"        # 접속토큰 폐기



# class TokenRequest(BaseModel):
#     url: str
#     api_key: str
#     app_secret: str




# @router.post("/get-token", tags=["auth"])
# async def get_token(request: TokenRequest):
#     print(f"url : {request.url}")
#     print(f"api_key : {request.api_key}")
#     print(f"app_secret : {request.app_secret}")
    
#     async with httpx.AsyncClient() as client:
#         response = await client.post(f"{request.url}{REQ_GET_ACCESS_TOKEN}", json={
#             "grant_type": "client_credentials",  # 고정 값
#             "appkey": request.api_key,
#             "appsecret": request.app_secret,
#         })
        
#         return response.json()




@router.post("/get-token", tags=["auth"])
async def get_token(api_key: str, app_secret: str):
    """API 키와 시크릿으로 토큰을 가져오거나 갱신"""
    try:
        # 서비스 레이어에서 토큰을 가져오거나 갱신하도록 요청
        token_info = await AuthService.get_or_refresh_token(api_key, app_secret, db_user=None)      # 필요하면 DB 추가
        return token_info
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
