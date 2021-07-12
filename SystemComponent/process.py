from time import sleep
from multiprocessing import Process, Queue

def work(in_queue: Queue, out_queu: Queue):
    while True:
        if not in_queue.empty():
            value = in_queue.get()
            if value < 0:
                return
            else:
                print(value)
                sleep(value)
                out_queu.put(value + 1)

if __name__ == "__main__":
    que1 = Queue()
    que2 = Queue()
    p = Process(target=work, args=(que1, que2))
    p.start()
    que1.put(1)
    que1.put(2)
    que1.put(3)
    que1.put(-1)
    p.join()
    while not que2.empty():
        ret = que2.get()
        print(ret)