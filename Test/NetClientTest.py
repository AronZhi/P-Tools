from NetComponent.ClientNet import *
from NetComponent.SessionFactory import *

def main():
    factory = SesionFactory()
    client = ClientNet('127.0.0.1', 8888, factory)
    asyncore.loop()

if __name__ == '__main__':
    main()