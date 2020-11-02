import asyncore
from .Msg import *

class Session(asyncore.dispatcher_with_send):
    def HandleData(self, data):
        print(data)
        return False

    def handle_read(self):
        data = self.recv(MsgMaxSize)
        self.HandleData(data.decode())