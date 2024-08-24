from dataclasses import asdict
from typing import Optional, Any, Generic, TypeVar, Union, List

from aiohttp import ClientSession, TCPConnector, ClientTimeout
from aiohttp.typedefs import StrOrURL, LooseCookies
from pydantic import BaseModel

T = TypeVar('T', bound=Union[BaseModel, List[BaseModel]])


class RestClient:
    _client: ClientSession

    def __init__(
            self,
            base_url: Optional[StrOrURL] = None,
            *,
            cookies: Optional[LooseCookies] = None,
            headers=None,
            **kwargs: Any
    ) -> None:
        if headers is None:
            headers = {}

        self._client = ClientSession(
            base_url=base_url,
            connector=TCPConnector(ssl=False),
            cookies=cookies,
            headers=headers,
            raise_for_status=True,
            timeout=ClientTimeout(3),
            **kwargs
        )

    async def __aenter__(self) -> "RestClient":
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self._client.close()

    async def close(self) -> None:
        await self._client.close()

    async def get_as_list(self, url: StrOrURL, response_type: Generic[T], **kwargs: Any) -> List[T]:
        res = await self._client.get(url, **kwargs)
        data = await res.json()
        return [item for item in map(lambda item: response_type(**item), data)]

    async def get(self, url: StrOrURL, response_type: Generic[T], **kwargs: Any) -> T:
        res = await self._client.get(url, **kwargs)
        data = await res.json()
        return response_type(**data)

    async def post(self, url, body: Any, response_type: Generic[T], **kwargs) -> T:
        res = await self._client.post(url, json=asdict(body), **kwargs)
        data = await res.json()
        return response_type(**data)

    async def put(self, url, body: Any, response_type: Generic[T], **kwargs) -> T:
        res = await self._client.put(url, json=asdict(body), **kwargs)
        data = await res.json()
        return response_type(**data)

    async def patch(self, url, body: Any, response_type: Generic[T], **kwargs) -> T:
        res = await self._client.patch(url, json=asdict(body), **kwargs)
        data = await res.json()
        return response_type(**data)

    async def delete(self, url, response_type: Generic[T], **kwargs) -> T:
        res = await self._client.delete(url, **kwargs)
        data = await res.json()
        return response_type(**data)