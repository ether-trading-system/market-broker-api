from typing import Callable, Any

from aiocache import caches, cached

caches.set_config({
    'default': {
        'cache': "aiocache.SimpleMemoryCache",
    }
})

cache = caches.get('default')


def cache_decorator(ttl: int) -> Callable:
    return cached(ttl=ttl, cache=cache)


async def get_cache(key: str) -> Any:
    try:
        return await cache.get(key)
    except Exception:
        return None


async def set_cache(key: str, value: Any, ttl: int = None) -> None:
    await cache.set(key, value, ttl=ttl)


async def delete_cache(key: str) -> None:
    await cache.delete(key)


async def clear_cache() -> None:
    await cache.clear()
