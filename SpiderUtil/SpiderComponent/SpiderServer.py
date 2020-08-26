from xmlrpc.server import SimpleXMLRPCServer
import socket
import threading
from SpiderComponent.Spider import *
from LogComponent.LogMember import *

class SpiderServer(threading.Thread):
    def __init__(self, port = 10000):
        threading.Thread.__init__(self)
        self.port = port
        hostname = socket.gethostname()
        self.localIP = socket.gethostbyname(hostname)
        self.server: SimpleXMLRPCServer = None


    def Init(self, worker: Spider):
        self.server = SimpleXMLRPCServer((self.localIP, self.port))
        self.server.register_instance(worker)
    

    def StopServer(self):
        if self.server:
            g_main_log.info('stop server')
            self.server.shutdown()


    def run(self):
        g_main_log.info('start listen %s:%d' % (self.localIP, self.port))
        self.server.serve_forever()    