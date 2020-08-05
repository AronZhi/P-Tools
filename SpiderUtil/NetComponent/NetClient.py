import asyncio

class NetClient(object):
    def __init__(self, host = '127.0.0.1', port = 10000):
        self.host = host
        self.port = port
        self.reader: asyncio.StreamReader = None
        self.writer: asyncio.StreamWriter = None


    def __del__(self):
        if self.writer:
            self.writer.close()

    def Disconnect(self):
        if self.writer:
            self.writer.close()
            self.writer = None


    async def Connect(self)->bool:
        self.reader, self.writer = await asyncio.open_connection(self.host, self.port)

        