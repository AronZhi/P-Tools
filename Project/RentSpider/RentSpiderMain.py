import threading
from LianjiaSpider import *
from SpiderComponent.Spider import Spider
from SpiderComponent.Spider import SpiderCtrl
from SpiderComponent.SpiderServer import SpiderServer


def CommondHandler(server: SpiderServer):
    commond = input('enter any to stop')
    server.StopServer()


def Work(spider):
    for index in range(1,100):
        url = 'https://hz.lianjia.com/zufang/pg%drco11/#contentList' % index
        if index == 1:
            url = 'https://hz.lianjia.com/zufang/rco11/#contentList'
        spider.Crawl(url)
        time.sleep(1)


def Test1():
    lianjiaHandler = LianjiaHandler()
    lianjiaHandler.InitDB()
    server = SpiderServer()
    server.SetServerWorker(SpiderCtrl(lianjiaHandler))
    commondThread = threading.Thread(target = CommondHandler, args={server,})
    server.start()
    commondThread.start()
    commondThread.join
    server.join()


def Test2():
    host = input('remote address(like 127.0.0.1:8000)    ')
    spider = Spider()
    spider.SetCtrl(remote = host)
    Work(spider)


def Test3():
    lianjiaHandler = LianjiaHandler()
    lianjiaHandler.InitDB()
    spider = Spider()
    spider.SetCtrl(page_handler = lianjiaHandler)
    Work(spider)


def main()->int:
    c = input('rpc server input 1, rpc client input 2, other run in local ')
    if c == '1':
        Test1()
    elif c == '2':
        Test2()
    else:
        Test3()
    return 0 

if __name__ == '__main__':
    main()
    