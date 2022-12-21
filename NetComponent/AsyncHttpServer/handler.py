import asyncio
from aiohttp import web
import weakref

async def on_shutdown(app: web.Application) -> None:
    print('on shutdown')
    sockets = weakref.WeakSet()
    for ws in sockets:
        await ws.close()

async def hello(request: web.Request):
    """
    # request body json form, and return json response
    data = await request.json()
    data["hello"] = "Hello, this is admin server"
    return web.json_response(text=json.dumps(data))
    """
    return web.Response(text="Hello, this is admin server")

async def stop(request: web.Request):
    exit(0)