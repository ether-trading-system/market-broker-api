from core.config_manager import config_manager

def get_kis_api_info():
    # KIS API 관련 설정 정보를 반환
    return {
        "base_url": config_manager.get_base_url(),
        "app_key": config_manager.get("KIS_APP_KEY"),
        "app_secret": config_manager.get("KIS_APP_SECRET")
    }
