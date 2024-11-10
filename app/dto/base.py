from typing import TypeVar, Generic, List

from pydantic import BaseModel
from pydantic.dataclasses import dataclass

T = TypeVar('T', bound=BaseModel)
U = TypeVar('U', bound=BaseModel)


@dataclass
class KisBaseResponse(Generic[T, U]):
    rt_cd: str
    msg_cd: str
    msg1: str
    ctx_area_fk100: str
    ctx_area_nk100: str
    output1: List[T]
    output2: List[U]
