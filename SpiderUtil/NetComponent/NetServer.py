import socket
import threading
from NetComponent.NetSession import *

class NetServer(object):
    def __init__(self, port = 10000):
        self.host = '127.0.0.1'
        self.port = port # port为0时，由系统决定端口
        self.socket = None

    def ConnectWith(self, clientSocket, ip):
        return

    def Run(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if self.socket:
            self.socket.bind((self.host, self.port))
            self.socket.listen()
            while True:
                clientSocket, clientIp = self.socket.accept()
                clientSocket.send('hello socket')
                data = clientSocket.recv(g_netDataSize)
                print(data)
                break
        return