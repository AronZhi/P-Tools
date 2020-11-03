from NetComponent.TCP.TcpServer import *
from NetComponent.TCP.SessionFactory import *

def main():
    factory = SessionFactory()
    server = TcpServer(8888, factory)
    server.Start()

if __name__ == '__main__':
    main()