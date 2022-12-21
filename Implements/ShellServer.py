import subprocess
import json
import asyncio
from aiohttp import web
import weakref


async def on_shutdown(app: web.Application) -> None:
    print('on shutdown')
    sockets = weakref.WeakSet()
    for ws in sockets:
        await ws.close()

async def processHello(request: web.Request):
    return web.Response(text="Hello, this is admin server")

async def processStop(request: web.Request):
    print("stop server")
    exit(0)

async def processShell(request: web.Request):
    param = await request.json()
    if command := param.get('command', None):
        print("execute: ", command)
        proc = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        proc.wait()
        output = proc.stdout.read()
        ret = output.decode('utf-8','replace')
        return web.json_response(text=json.dumps({"result": ret}))
    else:
        return web.json_response(text=json.dumps({"result": "param error"}))

class HttpServer(object):
    def __init__(self, event_loop, port=8888):
        self._event_loop = event_loop
        self._port = port
        self._app = web.Application()
        self._app.on_shutdown.append(on_shutdown)
        self._app.router.add_get('/hello', processHello)
        self._app.router.add_get('/stop', processStop)
        self._app.router.add_get('/shell', processShell)

    def run(self):
        web.run_app(app=self._app, port=self._port, loop=self._event_loop)


if __name__ == "__main__":
    """
    ctrl+c to stop app
    content type only support application/json
    """
    admin = HttpServer(asyncio.get_event_loop())
    admin.run()