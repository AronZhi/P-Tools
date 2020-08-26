from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import threading

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x // y

def ServerThread1(server):
    server.serve_forever()
    return True

def ServerThread2(server):
    input('enter any to stop')
    server.shutdown()
    return True

def Server():
    server = SimpleXMLRPCServer(("localhost", 8000))
    print("Listening on port 8000...")
    server.register_multicall_functions()
    server.register_function(add, 'add')
    server.register_function(subtract, 'subtract')
    server.register_function(multiply, 'multiply')
    server.register_function(divide, 'divide')
    serverThread = threading.Thread(target = ServerThread1, args = {server,})
    commandThread = threading.Thread(target = ServerThread2, args = {server,})
    serverThread.start()
    commandThread.start()
    commandThread.join()
    serverThread.join()
    

def Client():
    proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
    multicall = xmlrpc.client.MultiCall(proxy)
    multicall.add(7, 3)
    multicall.subtract(7, 3)
    multicall.multiply(7, 3)
    multicall.divide(7, 3)
    result = multicall()
    print("7+3=%d, 7-3=%d, 7*3=%d, 7//3=%d" % tuple(result))

if __name__ == '__main__':
    Server()