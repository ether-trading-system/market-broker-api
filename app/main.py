import uvicorn
from common import register_exception_handler
from fastapi import FastAPI
from .routers import accounts_router

app = FastAPI()
app.include_router(accounts_router)

# 예외처리 공통 메시지 등록
register_exception_handler(app)

@app.get("/")
async def root():
    return {"message": "Hello World"}


def start():
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
