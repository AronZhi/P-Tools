from Msg import *
from Spider import *

def test_1():
    msg = Msg()
    msg.data = 'hello'
    print(msg)

    jsonData = str(msg)
    msg2 = Msg()
    msg2.parse(jsonData)
    print(msg2.type)
    print(msg2.data)


def test_2():
    spider = Spider()
    spider.Crawl('https://book.douban.com/review/latest/')


def test_3():
    msg = Msg()
    msg.data = 'hello'

    netPack = NetPack()
    netPack.encode(str(msg), '127.0.0.1', 10000)
    print(netPack)
    text = str(netPack)
    print(len(text))

    netPack2 = NetPack()
    netPack2.parse(text)
    print(netPack2)


if __name__ == '__main__':
    test_3()