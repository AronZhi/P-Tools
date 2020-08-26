import xmlrpc.client
import threading
from SpiderComponent.Spider import *
from SpiderComponent.SpiderServer import *
from LogComponent.LogMember import g_main_log

class MySpider(Spider):
    def HandleMsg(self, url, msg: Msg):
        g_main_log.info(msg.data)
        return True


def CommondHandler(server: SpiderServer):
    commond = input('enter any to stop')
    server.StopServer()


def Test_Server():
    server = SpiderServer()
    spider = MySpider()
    server.Init(spider)
    commondThread = threading.Thread(target = CommondHandler, args={server,})
    server.start()
    commondThread.start()
    commondThread.join
    server.join()


def Test_Client():
    server = xmlrpc.client.ServerProxy('10.224.203.49:10000', verbose=True)
    ret = server.Crawl('https://www.runoob.com/python3/python3-file-methods.html')
    print(ret)


def Test_local():
    spider = MySpider()
    spider.Crawl('https://www.runoob.com/python3/python3-file-methods.html')


if __name__ == '__main__':
    Test_Client()