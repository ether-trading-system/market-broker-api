from dataclasses import field
from pydantic.dataclasses import dataclass
from pydantic import Field
from typing import Optional


@dataclass
class SubscribeResponseHeader:
    """전송한 tr_id"""
    tr_id: str

    """전송한 tr_key"""
    tr_key: str

    """N"""
    encrypt: str

    datetime: Optional[str] = field(default=None)


@dataclass
class SubscribeResponseBodyOutput:
    iv: str
    key: str


@dataclass
class SubscribeResponseBody:
    rt_cd: str

    msg_cd: str

    msg1: str

    output: Optional[SubscribeResponseBodyOutput] = Field(None)


@dataclass
class SubscribeResponse:
    header: SubscribeResponseHeader

    body: Optional[SubscribeResponseBody] = field(default=None)