import asyncore
from .SessionManager import SessionManager

class ServerNet(asyncore.dispatcher):
    def __init__(self, host, port, sessionCount, sessionManager:SessionManager):
        asyncore.dispatcher.__init__(self)
        self.sessionMgr = sessionManager
        self.create_socket()
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(sessionCount)
    
    def handle_accepted(self, sock, addr):
        handler = self.sessionMgr.CreateSession(sock, addr)
        accept_msg = 'accept {ip}:{port}'.format(ip = addr[0], port = addr[1])
        handler.send(accept_msg.encode())