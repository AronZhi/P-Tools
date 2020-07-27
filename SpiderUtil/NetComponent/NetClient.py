import socket
from NetComponent.NetSession import *


class NetClient(object):
    def __init__(self, host = '127.0.0.1', port = 10000):
        self.host = host
        self.port = port
        self.socket = None

    def Connect(self)->bool:
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if self.socket:
            self.socket.connect((self.host, self.port))
            return True
        return False

    def Disconnect(self):
        if self.socket:
            self.socket.close()

    
    def Send(self, data):
        if self.socket:
            self.socket.send(data)

    
    def Receive(self):
        if self.socket:
            data = self.socket.recv(g_netDataSize)
            return data
        return ''
        