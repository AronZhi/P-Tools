from SpiderComponent.Spider import *

class MySpider(Spider):
    def HandleMsg(self, url, msg: Msg):
        print(msg.data)
        return True


def main():
    spider = MySpider()
    spider.Crawl('https://www.runoob.com/python3/python3-file-methods.html')
    return


if __name__ == '__main__':
    main()