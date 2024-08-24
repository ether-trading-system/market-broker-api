import pytest

from core import RestClient
from typing import Optional, Protocol
from pydantic import ValidationError
from pydantic.dataclasses import dataclass


# {
#     "title": "Black Coffee",
#     "description": "Svart kaffe är så enkelt som det kan bli med malda kaffebönor dränkta i hett vatten, serverat varmt. Och om du vill låta fancy kan du kalla svart kaffe med sitt rätta namn: café noir.",
#     "ingredients": [
#       "Coffee"
#     ],
#     "image": "https://images.unsplash.com/photo-1494314671902-399b18174975?auto=format&fit=crop&q=80&w=1887&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
#     "id": 1
#   }

@pytest.mark.asyncio
async def test_get_as_list():
    @dataclass
    class Coffee(Protocol):
        title: Optional[str]
        description: Optional[str]
        ingredients: list[str]
        image: Optional[str]
        id: int

    async with RestClient() as client:
        response = await client.get_as_list('https://api.sampleapis.com/coffee/hot', response_type=Coffee)

        assert response is not None
        assert len(response) > 0
        assert response[0].title is not None
        assert response[0].description is not None


@pytest.mark.asyncio
async def test_get_as_list_validation_error():
    @dataclass
    class Coffee(Protocol):
        title: Optional[int]
        description: Optional[str]
        ingredients: list[str]
        image: Optional[str]
        id: int

    with pytest.raises(ValidationError) as error_info:
        async with RestClient() as client:
            await client.get_as_list('https://api.sampleapis.com/coffee/hot', response_type=Coffee)

    assert 'title' in str(error_info.value)
