import asyncio
from .SessionFactory import SessionFactory

class TcpServer(object):
    def __init__(self, port, sessionFactory: SessionFactory, host = '127.0.0.1'):
        self.host = host
        self.port = port
        self.factory = sessionFactory

    async def run(self):
        loop = asyncio.get_running_loop()
        server = await loop.create_server(self.factory.Create, self.host, self.port)
        try:
            async with server:
                await server.serve_forever()
        finally:
            server.close()
    
    def Start(self):
        asyncio.run(self.run())