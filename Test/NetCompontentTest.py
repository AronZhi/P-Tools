from NetComponent.NetServer import NetServer
from NetComponent.NetClient import NetClient

def test_1():
    server = NetServer(0)
    server.Run()
    print('start')
    input()
    return

def test_2():
    client = NetClient()
    client.Connect()
    print(client.Receive())
    client.Send('hello')
    client.Disconnect()

if __name__ == '__main__':
    test_2()