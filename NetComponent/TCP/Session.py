import asyncio

class Session(asyncio.Protocol):
    def __SetTransport(self, transport: asyncio.Transport):
        self.transport = transport

    def Handle(self, message):
        print(message)
        self.transport.write(message.encode())
        self.transport.close()
        return False

    def connection_made(self, transport: asyncio.Transport):
        self.__SetTransport(transport)
        message = 'test test test'
        self.transport.write(message.encode())

    def data_received(self, data):
        self.Handle(data.decode())