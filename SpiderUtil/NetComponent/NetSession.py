import socket

g_netDataSize = 1024

class NetSession(object):
    def __init__(self, ip, netSocket: socket.socket):
        self.ip = ip
        self.socket = netSocket