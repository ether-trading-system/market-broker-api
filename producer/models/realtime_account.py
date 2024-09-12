from dataclasses import dataclass


@dataclass
class RealtimeAccount:
    account_id: int
    app_key: str
    app_secret: str
    hts_id: str
    websocket_key: str
