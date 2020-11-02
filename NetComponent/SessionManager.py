from .SessionFactory import SesionFactory
from .Session import Session

class SessionManager():
    def __init__(self, factory:SesionFactory):
        self.sessions = dict()
        self.factory = factory
    
    def CreateSession(self, sock, addr)->Session:
        handler = self.factory.Create(sock)
        self.sessions[addr] = handler
        return handler