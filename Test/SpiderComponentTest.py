from SpiderComponent.Spider import *
from LogComponent.LogMember import g_main_log

class MySpider(Spider):
    def HandleMsg(self, url, msg: Msg):
        g_main_log.info(msg.data)
        return True


def main():
    spider = MySpider()
    spider.Crawl('https://www.runoob.com/python3/python3-file-methods.html')
    return


if __name__ == '__main__':
    main()