import asyncio
from aiohttp import web
from handler import *

class AdminServer(object):
    def __init__(self, port=8888, event_loop = None):
        if event_loop is None:
            """
            windows环境python3.7及以上版本tornado使用asyncio可能抛出NotImplementedError异常, 使用前需要以下处理
            if psutil.WINDOWS and sys.version_info >= (3,7):
                asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
            """
            self._event_loop = asyncio.get_event_loop()
        else:
            self._event_loop = event_loop
        self._port = port
        self._app = web.Application()
        self._app.on_shutdown.append(on_shutdown)
        self._app.router.add_get('/hello', hello)
        self._app.router.add_get('/stop', stop)

    def run(self):
        web.run_app(app=self._app, port=self._port, loop=self._event_loop)