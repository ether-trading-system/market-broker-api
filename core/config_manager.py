class ConfigManager:
    """ 전역 설정 관리용 Singleton Class """
    
    _instance = None
    _config = {
        "URL_KIND": "simulate",  # 기본값을 simulate로 설정
        "KIS_APP_KEY": "",
        "KIS_APP_SECRET": ""
    }
    
    # 모의투자 url과 실전투자 url을 미리 정의
    _urls = {
        "simulate": "https://openapivts.koreainvestment.com:29443",
        "real": "https://openapi.koreainvestment.com:9443"
    }
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
        return cls._instance
    
    def get(self, key: str):
        return self._config.get(key)
    
    def set(self, key: str, value):
        self._config[key] = value

    def get_base_url(self):
        """ url_kind에 따른 BASE_URL을 반환하는 메서드 """
        kind = self._config.get("url_kind", "simulate")  # 기본값 'simulate'
        return self._urls.get(kind)

# Singleton 인스턴스 생성
config_manager = ConfigManager()
