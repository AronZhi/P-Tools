import multiprocessing
import time
import os

def producer(msgQueue):
    pid = os.getpid()
    for index in range(5):
        if not msgQueue.full():
            msg = '%d: %s' % (pid, time.ctime())
            msgQueue.put_nowait(msg)
            time.sleep(1)
    
    if not msgQueue.full():
            msgQueue.put_nowait('stop')
    return


def handleMsg(msg):
    if msg == 'stop':
        return True
    else:
        print(msg)
        return False


def consumer(msgQueue):
    stop = False
    while not stop:
        if msgQueue.empty():
            continue
        stop = handleMsg(msgQueue.get_nowait())
    print('end')


def main():
    msgQueue = multiprocessing.Queue(100)
    c = multiprocessing.Process(target = consumer, args=(msgQueue,))
    p = multiprocessing.Process(target = producer, args=(msgQueue,))
    c.start()
    p.start()
    p.join()
    c.join()
    return


if __name__ == '__main__':
    main()