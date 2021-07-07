from time import sleep, time
import psutil

class PerformanceInfo(object):
    def GetCpuPercent(self):
        return psutil.cpu_percent(interval=2, percpu=True)
    
    def GetMemoryPercent(self):
        return psutil.virtual_memory().percent
    
    def GetProcessRunInfo(self, process_name):
        cpu_percent = 0
        memory_usage = 0
        process_list =[]
        for process in psutil.process_iter():
            try:
                if process_name.lower() == process.name().lower():
                    process_list.append(process)
                    memory_usage += process.memory_info().rss
            except (psutil.AccessDenied, psutil.ZombieProcess):
                continue
        for process in process_list:
            cpu_percent += process.cpu_percent(None)
        sleep(2)
        for process in process_list:
            cpu_percent += process.cpu_percent(None)
        return cpu_percent, memory_usage

"""
if __name__ == "__main__":
    performanceInfo = PerformanceInfo()
    print(performanceInfo.GetCpuPercent())
    print(performanceInfo.GetMemoryPercent())
    print(performanceInfo.GetProcessRunInfo('firefox'))
"""