from uuid import uuid4
from time import sleep, time
from threading import Thread
from json import loads, dumps
from random import getrandbits
from websocket import WebSocketApp
from requests import Session


class Perplexity:
    def __init__(self):
        self.session = Session()
        self.request_headers = {
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }
        self.session.headers.update(self.request_headers)
        self.t = format(getrandbits(32), "08x")
        self.sid = loads(
            self.session.get(
                url=f"https://www.perplexity.ai/socket.io/?EIO=4&transport=polling&t={self.t}"
            ).text[1:]
        )["sid"]
        self.n = 1
        self.base = 420
        self.finished = True
        self.last_uuid = None
        assert (
            lambda: self.session.post(
                url=f"https://www.perplexity.ai/socket.io/?EIO=4&transport=polling&t={self.t}&sid={self.sid}",
                data='40{"jwt":"anonymous-ask-user"}',
            ).text
            == "OK"
        )(), "Failed to ask the anonymous user."
        self.ws = self._init_websocket()
        self.ws_thread = Thread(target=self.ws.run_forever).start()
        while not (self.ws.sock and self.ws.sock.connected):
            sleep(0.1)

    def _init_websocket(self):
        def on_open(ws):
            ws.send("2probe")
            ws.send("5")

        def on_message(ws, message):
            if message == "2":
                ws.send("3")
            elif not self.finished:
                if message.startswith("42"):
                    message = loads(message[2:])
                    content = message[1]
                    if "mode" in content:
                        content.update(loads(content["text"]))
                    content.pop("text")
                    if (not ("final" in content and content["final"])) or (
                        "status" in content and content["status"] == "completed"
                    ):
                        self.queue.append(content)
                    if message[0] == "query_answered":
                        self.last_uuid = content["uuid"]
                        self.finished = True
                elif message.startswith("43"):
                    message = loads(message[3:])[0]
                    if (
                        "uuid" in message and message["uuid"] != self.last_uuid
                    ) or "uuid" not in message:
                        self.queue.append(message)
                        self.finished = True

        cookies = ""
        for key, value in self.session.cookies.get_dict().items():
            cookies += f"{key}={value}; "
        return WebSocketApp(
            url=f"wss://www.perplexity.ai/socket.io/?EIO=4&transport=websocket&sid={self.sid}",
            header=self.request_headers,
            cookie=cookies[:-2],
            on_open=on_open,
            on_message=on_message,
            on_error=lambda ws, err: print(f"WebSocket error: {err}"),
        )

    def generate_answer(self, query):
        self.finished = False
        if self.n == 9:
            self.n = 0
            self.base *= 10
        else:
            self.n += 1
        self.queue = []
        self.ws.send(
            str(self.base + self.n)
            + dumps(
                [
                    "perplexity_ask",
                    query,
                    {
                        "frontend_session_id": str(uuid4()),
                        "language": "en-GB",
                        "timezone": "UTC",
                        "search_focus": "internet",
                        "frontend_uuid": str(uuid4()),
                        "mode": "concise",
                    },
                ]
            )
        )
        start_time = time()
        while (not self.finished) or len(self.queue) != 0:
            if time() - start_time > 30:
                self.finished = True
                return {"error": "Timed out."}
            if len(self.queue) != 0:
                yield self.queue.pop(0)
        self.ws.close()
