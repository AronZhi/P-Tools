from .Session import Session

class SesionFactory():
    def Create(self, sock):
        return Session(sock)