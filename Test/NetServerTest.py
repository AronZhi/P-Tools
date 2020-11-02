from NetComponent.ServerNet import *
from NetComponent.SessionManager import *
from NetComponent.SessionFactory import *

def main():
    mgr = SessionManager(SesionFactory())
    server = ServerNet('127.0.0.1', 8888, 5, mgr)
    asyncore.loop()

if __name__ == '__main__':
    main()