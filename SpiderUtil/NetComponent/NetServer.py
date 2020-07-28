import socket
import threading
from NetComponent.NetSession import *

class NetServer(object):
    def __init__(self, port = 10000):
        self.host = socket.gethostbyname(socket.gethostname())
        self.port = port # port为0时，由系统决定端口
        self.socket = None
        self.runlock = threading.Lock()
        self.stop = False

    def __del__(self):
        if self.socket:
            self.socket.close()


    def Stop(self):
        self.runlock.acquire()
        self.stop = True
        self.runlock.release()

    
    def IsStop(self):
        self.runlock.acquire()
        isStop = self.stop
        self.runlock.release()
        return isStop


    def Run(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if self.socket:
            self.socket.bind((self.host, self.port))
            self.socket.listen()
            print('listen %s:%d' % (self.host, self.port))
            while not self.IsStop():
                clientSocket, clientIp = self.socket.accept()
                session = NetSession(clientSocket, clientIp)
                session.Communicate()
        return