from .Session import Session

class SessionFactory(object):
    def Create(self)->Session:
        return Session()