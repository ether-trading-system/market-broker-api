import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from core.config_manager import config_manager

app = FastAPI()

# 테스트용 설정 값을 설정
config_manager.set("KIS_BASE_URL", "https://openapi.koreainvestment.com:9443")
config_manager.set("KIS_REAL_APP_KEY", "aaa")
config_manager.set("KIS_REAL_APP_SECRET", "bbb")

# 테스트할 엔드포인트 정의
@app.get("/get-env-info")
async def get_env_info():
    # ConfigManager에서 설정 값을 가져와서 반환
    return {
        "kis_base_url": config_manager.get("KIS_BASE_URL"),
        "kis_real_app_key": config_manager.get("KIS_REAL_APP_KEY"),
        "kis_real_app_secret": config_manager.get("KIS_REAL_APP_SECRET")
    }


client = TestClient(app)


# 테스트 함수 정의
def test_env_info():
    response = client.get("/get-env-info")
    assert response.status_code == 200  # 상태 코드가 200인지 확인
    
    # 예상된 설정 정보와 비교
    expected_response = {
        "kis_base_url": "https://openapi.koreainvestment.com:9443",
        "kis_real_app_key": "test_app_key111",
        "kis_real_app_secret": "test_app_secret123"
    }
    
    # 응답 결과 출력 및 검증
    print("Response JSON:", response.json())
    assert response.json() == expected_response  # 응답 값이 예상된 값과 일치하는지 확인
