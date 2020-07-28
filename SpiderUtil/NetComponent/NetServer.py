import socket
from threading import Lock
from NetComponent.NetSession import *

class NetServer(object):
    def __init__(self, port = 10000):
        self.host = socket.gethostbyname(socket.gethostname())
        self.port = port # port为0时，由系统决定端口
        self.socket = None
        self.runlock = Lock()
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
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if self.socket:
                self.socket.bind((self.host, self.port))
                self.socket.listen()
                print('listen %s:%d' % (self.host, self.port))
                self.socket.settimeout(5)
                while not self.IsStop():
                    try:
                        clientSocket, clientIp = self.socket.accept()
                        print(clientIp)
                        session = NetSession(clientSocket, clientIp)
                        session.Communicate()
                    except socket.timeout:
                        print('wait long time')
                        pass
            
                self.socket.close()
                self.socket = None

        except Exception as e:
            print('server run error coour: %s' % e)
        
        return