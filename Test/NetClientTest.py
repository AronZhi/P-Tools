from NetComponent.TCP.TcpClient import *
from NetComponent.TCP.SessionFactory import *
from NetComponent.Common import *

def main():
    factory = SessionFactory()
    client = TcpClient('127.0.0.1', 8888, factory)
    client.Start()

if __name__ == '__main__':
    main()