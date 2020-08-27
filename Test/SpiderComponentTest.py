import xmlrpc.client
import threading
from SpiderComponent.Spider import Spider
from SpiderComponent.SpiderServer import SpiderServer
from SpiderComponent.SpiderHandler import SpiderHandler
from MsgComponent.Msg import Msg
from LogComponent.LogMember import g_main_log

class MySpiderHandler(SpiderHandler):
    def HandleMsg(self, url, msg: Msg):
        g_main_log.info(url)
        return True


def CommondHandler(server: SpiderServer):
    commond = input('enter any to stop')
    server.StopServer()


def Test_Server():
    server = SpiderServer()
    myHandler = MySpiderHandler()
    server.Init(myHandler)
    commondThread = threading.Thread(target = CommondHandler, args={server,})
    server.start()
    commondThread.start()
    commondThread.join
    server.join()


def Test_Client():
    host = input('remote address(like 127.0.0.1:8000)    ')
    spider = Spider()
    spider.SetPartner(remote = host)
    ret = spider.Crawl('https://www.runoob.com/python3/python3-file-methods.html')
    print(ret)


def Test_local():
    spider = Spider()
    handler = MySpiderHandler()
    spider.SetHandler(local = handler)
    spider.Crawl('https://www.runoob.com/python3/python3-file-methods.html')


if __name__ == '__main__':
    choice = input('client input 1, server input 2, local input other:   ')
    if choice == '1':
        Test_Client()
    elif choice == '2':
        Test_Server()
    else:
        Test_local()