import platform
import psutil
import os
import socket

class SystemInfo(object):
    def __init__(self) -> None:
        self.hostName = None
        self.localIP = None

    def GetOSInfo(self):
        os = platform.system()
        versionInfo = platform.version()
        version = versionInfo.split('.')
        bitInfo = platform.machine()
        bit = 32
        if '64' in bitInfo:
            bit = 64
        elif '86' in bit:
            bit = 32
        return os, version[0], bit
    
    def GetHostName(self):
        if not self.hostName:
            self.hostName = socket.gethostname()
        return self.hostName
    
    def GetLocalIP(self):
        if not self.localIP:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            self.localIP = s.getsockname()[0]
        return self.localIP
    
    def GetMacAddress(self):
        import uuid
        mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
        return ":".join([mac[e:e+2] for e in range(0,11,2)])
    
    def GetCPUInfo(self):
        cpu_info = dict()
        cpu_info['name'] = platform.processor()
        cpu_info['count'] = psutil.cpu_count(logical=False)  # cpu核心数
        cpu_info['thread'] = psutil.cpu_count()  # cpu线程数
        cpu_info['frequency'] = psutil.cpu_freq()[2] / 1000  # 频率MHZ
        #cpu_info['usage'] = psutil.cpu_percent()  # cpu使用率
        return cpu_info

"""
if __name__ == "__main__":
    test = SystemInfo()
    print(test.GetOSInfo())
    print(test.GetHostName())
    print(test.GetLocalIP())
    print(test.GetMacAddress())
"""