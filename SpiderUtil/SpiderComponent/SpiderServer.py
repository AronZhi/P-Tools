from xmlrpc import SimpleXMLRPCServer
import socket
from SpiderComponent.Spider import Spider
from LogComponent.LogMember import *

class SpiderServer(object):
    def __init__(self, port = 10000):
        self.port = port

    def _getLocalIP(self):
        hostname = socket.gethostname()
        localIP = socket.gethostbyname(hostname)
        return localIP

    def Work(self, spider: Spider):
        localIP = self._getLocalIP()
        server = SimpleXMLRPCServer.SimpleXMLRPCServer((localIP, self.port))
        server.register_instance(spider)
        g_main_log.info('start listen %s:%d' % (localIP, self.port)
        self.server.serve_forever()