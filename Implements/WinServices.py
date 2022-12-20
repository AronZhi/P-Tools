import win32service
import win32serviceutil

class ServiceStatus:
    STOPPED = win32service.SERVICE_STOPPED or 1
    START_PENDING = win32service.SERVICE_START_PENDING or 2
    STOP_PENDING = win32service.SERVICE_STOP_PENDING or 3
    RUNNING = win32service.SERVICE_RUNNING or 4

class WinService(object):
    def __init__(self, service_name: str):
        self.service_name = service_name

    def status(self):
        if res := win32serviceutil.QueryServiceStatus(self.service_name):
            return res[1]
        else:
            return None
    
    def start(self):
        if self.status() == ServiceStatus.STOPPED:
            win32serviceutil.StartService(self.service_name)
    
    def stop(self):
        if self.status() == ServiceStatus.RUNNING:
            win32serviceutil.StopService(self.service_name)
        

if __name__ == "__main__":
    srv = WinService("Wcmsvc")
    print(srv.status())