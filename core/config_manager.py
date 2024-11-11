class ConfigManager:
    """ 전역 설정 관리용 Sigleton Class """
    _instance = None
    _config ={
        "BASE_URL" : "",
        "KIS_APP_KEY" : "",
        "KIS_APP_SECRET" : ""
    }
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
        return cls._instance
    
    def get(self, key: str):
        return self._config.get(key)
    
    def set(self, key: str, value):
        self._config[key] = value


config_manager = ConfigManager()