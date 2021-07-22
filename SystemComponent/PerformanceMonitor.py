from multiprocessing import Process, Queue
import time
from Performance import PerformanceInfo

def work(pro_names, queue):
    performanceInfo = PerformanceInfo()
    process_list = performanceInfo.GetProcess(pro_names)
    if len(process_list) == 0:
        print("can not find process")
        return
    while True:
        if not queue.empty():
            msg = queue.get()
            if msg.lower() == "stop":
                print("stop mointoring")
                return
        print(performanceInfo.GetProcessMemoryUsage(process_list))
        print(performanceInfo.GetProcessCpuPercent(process_list))

class PerformanceMonitor(object):
    def __init__(self):
        self.msq_que = Queue()
        self.monitor: Process = None
    
    def __del__(self):
        if self.monitor:
            self.stop()
    
    def start(self, process_names: list):
        self.monitor = Process(target=work, args=(process_names, self.msq_que))
        self.monitor.start()
    
    def stop(self):
        self.msq_que.put("stop")
        self.monitor.join()
        self.monitor = None

"""
if __name__ == "__main__":
    monitor = PerformanceMonitor()
    monitor.start(["firefox"])
    time.sleep(10)
    monitor.stop()
"""