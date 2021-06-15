import psutil

class PerformanceInfo(object):
    def GetCpuPercent(self):
        return psutil.cpu_percent(interval=0.5, percpu=True)
    
    def GetMemoryPercent(self):
        return psutil.virtual_memory().percent
    
    def GetProcessRunInfo(self, process_name):
        cpu_percent = 0
        memory_usage = 0
        for process in psutil.process_iter():
            try:
                if process_name.lower() in process.name().lower():
                    cpu_percent += process.cpu_percent()
                    memory_usage += process.memory_info().rss
            except (psutil.AccessDenied, psutil.ZombieProcess):
                continue
        return cpu_percent, memory_usage

"""
if __name__ == "__main__":
    performanceInfo = PerformanceInfo()
    print(performanceInfo.GetCpuPercent())
    print(performanceInfo.GetMemoryPercent())
    print(performanceInfo.GetProcessRunInfo('firefox'))
"""
