import socket
from NetComponent.NetSession import *

class NetClient(object):
    def __init__(self, host = '127.0.0.1', port = 10000):
        self.host = host
        self.port = port
        self.socket = None


    def __del__(self):
        if self.socket:
            self.socket.close()


    def Connect(self)->bool:
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if self.socket:
            self.socket.connect((self.host, self.port))
            session = NetSession(self.socket, self.host)
            session.Communicate()
            return True
        return False


    def Disconnect(self):
        if self.socket:
            self.socket.close()
            self.socket = None
        