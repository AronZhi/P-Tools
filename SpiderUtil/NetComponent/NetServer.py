import socket
import threading
from NetComponent.NetSession import *

class NetServer(object):
    def __init__(self, port = 10000):
        self.host = socket.gethostbyname(socket.gethostname())
        self.port = port # port为0时，由系统决定端口
        self.socket = None


    def __del__(self):
        if self.socket:
            self.socket.close()


    def Communicate(self, clientSocket: socket.socket, data:str):
        if clientSocket:
            clientSocket.send(data.encode('utf8'))
            data = clientSocket.recv(g_netDataSize)
            print(data.decode('utf8'))
        return


    def Run(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if self.socket:
            self.socket.bind((self.host, self.port))
            self.socket.listen()
            print('listen %s:%d' % (self.host, self.port))
            clientSocket, clientIp = self.socket.accept()
            self.Communicate(clientSocket, 'hello client')
        return