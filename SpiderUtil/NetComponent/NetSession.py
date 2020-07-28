import socket

g_netDataSize = 1024

class NetSession(object):
    def __init__(self, remotSocket: socket.socket, remoteIp):
        self.remotSocket = remotSocket
        self.remoteIp = remoteIp


    def SendData(self, data: str):
        bytedata = data.encode('utf8')
        self.remotSocket.send(bytedata)



    def RecvData(self):
        bytedata = self.remotSocket.recv(g_netDataSize)
        data = bytedata.decode('utf8')
        return data


    def Communicate(self):
        if self.remotSocket:
            self.SendData('hello socket')
            data = self.RecvData()
            print(data)  