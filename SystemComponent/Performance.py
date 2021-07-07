from time import sleep, time
import psutil

class PerformanceInfo(object):
    def GetCpuPercent(self):
        return psutil.cpu_percent(interval=2, percpu=True)
    
    def GetMemoryPercent(self):
        return psutil.virtual_memory().percent
    
    def GetProcess(self, process_name):
        process_list =[]
        for process in psutil.process_iter():
            try:
                if process_name.lower() == process.name().lower():
                    process_list.append(process)
            except (psutil.AccessDenied, psutil.ZombieProcess):
                continue
        return process_list
    
    def GetProcessMemoryUsage(self, process_list):
        memory_usage = 0.0
        for process in process_list:
            memory_usage += process.memory_info().rss
        return memory_usage
    
    def GetProcessCpuPercent(self, process_list):
        cpu_percent = 0.0
        for process in process_list:
            cpu_percent += process.cpu_percent(None)
        sleep(2)
        for process in process_list:
            cpu_percent += process.cpu_percent(None)
        return cpu_percent

"""
if __name__ == "__main__":
    performanceInfo = PerformanceInfo()
    print(performanceInfo.GetCpuPercent())
    print(performanceInfo.GetMemoryPercent())
    process_list = performanceInfo.GetProcess('firefox.exe')
    print(performanceInfo.GetProcessCpuPercent(process_list))
    print(performanceInfo.GetProcessMemoryUsage(process_list))
"""