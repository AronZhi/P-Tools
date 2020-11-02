import asyncore
from .SessionFactory import SesionFactory

class ClientNet(asyncore.dispatcher):
    def __init__(self, host, port, sessionFactory: SesionFactory):
        asyncore.dispatcher.__init__(self)
        self.factory = sessionFactory
        self.create_socket()
        self.connect((host, port))

    def handle_connect(self):
        handler = self.factory.Create(self.socket)
        connect_msg = 'connect success'
        handler.send(connect_msg.encode())