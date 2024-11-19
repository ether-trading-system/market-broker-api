from fastapi import FastAPI
from sample.api.member import user, auth_kis, auth_kakao
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS 설정 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # 필요한 도메인을 추가합니다.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 추가
app.include_router(auth_kis.router, prefix="/public/api/borker/auth_kis", tags=["auth_KIS"])
app.include_router(auth_kakao.router, prefix="/public/api/borker/auth_kakao", tags=["auth_Kakao"])
app.include_router(user.router, prefix="/public/api/borker/user", tags=["user"])
