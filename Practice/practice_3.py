import multiprocessing
import time
import os

def workFunc(loopCount, interval):
    pid = os.getpid()
    while loopCount > 0:
        print('%d, %s: %d' % (pid, time.ctime(), loopCount))
        time.sleep(interval)
        loopCount -= 1

def test_1():
    p = multiprocessing.Process(target = workFunc, args = (3, 1))
    p.start()
    print('main process pid:%d' % os.getpid())
    print('sub process pid: %d' % p.pid)
    print('sub process name: %s' % p.name)
    p.join()
    print('test_1 end')

if __name__ == "__main__":
    test_1()