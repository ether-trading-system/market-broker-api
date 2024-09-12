import logging

from typing import List
from domain.kis import KisAuthRest
from domain.kis.kis_websocket_client import connect
from .models import RealtimeAccount

logger = logging.getLogger('producer')


class MarketBrokerDispatcher:
    _accounts: List[RealtimeAccount]

    def __init__(self, accounts):
        self._accounts = accounts

    @staticmethod
    async def create() -> "MarketBrokerDispatcher":
        app_key = ''
        app_secret = ''
        hts_id = ''
        async with KisAuthRest() as rest:
            response = await rest.get_websocket_key(
                app_key=app_key,
                app_secret=app_secret
            )
            logger.debug(response.approval_key)
            return MarketBrokerDispatcher([
                RealtimeAccount(
                    account_id=1,
                    app_key=app_key,
                    app_secret=app_secret,
                    hts_id=hts_id,
                    websocket_key=response.approval_key
                )])

    async def start(self):
        for account in self._accounts:
            await connect(account.websocket_key)
        logger.info("MarketBrokerDispatcher started")
