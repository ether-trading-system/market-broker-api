import asyncio
import logging
import sys

from producer.dispatcher import MarketBrokerDispatcher

logger = logging.getLogger('producer')
logger.setLevel(logging.DEBUG)


async def main():
    dispatcher = await MarketBrokerDispatcher.create()
    await dispatcher.start()


def init_logger():
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)


if __name__ == '__main__':
    init_logger()
    asyncio.run(main())
