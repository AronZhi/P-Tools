import asyncio
from .SessionFactory import SessionFactory

class TcpClient(object):
    def __init__(self, host, port, sessionFactory:SessionFactory):
        self.host = host
        self.port = port
        self.factory = sessionFactory

    async def run(self):
        loop = asyncio.get_running_loop()
        transport, protocol = await loop.create_connection(self.factory.Create, self.host, self.port)
    
    def Start(self):
        asyncio.run(self.run())