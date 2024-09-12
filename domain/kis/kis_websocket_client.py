from typing import Optional

import websockets as ws
from websockets.exceptions import ConnectionClosedError
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64decode

from core import settings
from domain.kis.dto.websocket import SubscribeResponse


def get_tr_id(resource: str):
    tr_id_map = {
        'prod': {
            'inquire-balance': 'H0STCNI0'
        },
        'dev': {
            'inquire-balance': 'H0STCNI9'
        }
    }

    if settings.env == 'prod':
        return tr_id_map['prod'][resource]

    return tr_id_map['dev'][resource]


MAX_RECONNECTS = 5
MAX_RECONNECT_SECONDS = 60
MIN_RECONNECT_WAIT = 0.1
TIMEOUT = 10
NO_MESSAGE_RECONNECT_TIMEOUT = 60
MAX_QUEUE_SIZE = 100


async def connect(key: str):
    async with ws.connect(settings.kis_websocket_url, ping_interval=60) as websocket:
        header = {
            "approval_key": key,
            "custtype": "P",
            "tr_type": "1",
            "content-type": "utf-8"
        }

        body = {
            "input": {
                "tr_id": "H0STCNI9",
                "tr_key": "dalcon",
            }
        }

        await websocket.send(json.dumps({"header": header, "body": body}))

        while True:
            try:
                await handle_message(websocket, await websocket.recv())
                # subscribe_response = SubscribeResponse(**response)
            except ConnectionClosedError:
                print("Connection closed")
                break
            except Exception as e:
                print("Error")
                print(e)
                break


async def handle_message(ws, message: str):
    data = json.loads(message)
    print(data)
    # {'header': {'tr_id': 'H0STCNI9', 'tr_key': 'dalcon', 'encrypt': 'N'}, 'body': {'rt_cd': '0', 'msg_cd': 'OPSP0000', 'msg1': 'SUBSCRIBE SUCCESS', 'output': {'iv': 'cab1c2d7d66ea8eb', 'key': 'ikznadvwtxbbvoletwjafmzlwcviuyhe'}}}

    header = data['header']
    body = data.get('body')

    tr_id = header['tr_id']
    tr_key: Optional[str] = header.get('tr_key')

    if tr_id == 'PINGPONG':
        print(f"PingPong: {data}")
        await ws.send(json.dumps(data))
        return

    if not body:
        print(f"Not body: {data}")
        return

    code = body["msg_cd"]
    message = body["msg1"]
    output = body.get("output")

    match code:
        case "OPSP0000":  # subscribed
            print("RTC Subscribed to %s")
        case "OPSP0002":  # already subscribed
            print("RTC Already subscribed to %s")
        case "OPSP0001":  # unsubscribed
            print("RTC Unsubscribed from %s")

        case "OPSP0003":  # not subscribed
            print("RTC Not subscribed to %s")
        case "OPSP8996":  # already in use
            print("RTC Session already in use")

        case "OPSP0007":  # internal error
            print("RTC Internal server error: %s %s")

        case "OPSP9999":
            # {'header': {'tr_id': '(null)', 'tr_key': '', 'encrypt': 'N'}, 'body': {'rt_cd': '9', 'msg_cd': 'OPSP9999', 'msg1': 'JSON PARSING ERROR : invalid json format'}}
            print("RTC Unknown error: %s %s")
        case "OPSP8993":
            # {'header': {'tr_id': '', 'tr_key': '', 'encrypt': 'N'}, 'body': {'rt_cd': '9', 'msg_cd': 'OPSP8993', 'msg1': 'JSON PARSING ERROR : invalid tr_key'}}
            print("RTC Invalid tr_key: %s %s")
        case _:
            print("RTC Unhandled control message: %s(%s) %s")


