import socket

def GetLocalIP():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 10000))
        localIP = s.getsockname()[0]
        return localIP
    finally:
        s.close()