from Spider import *
from Parse import *
from Decoration import *

def TestDouBanByHeader():
    decoration = Decoration()
    spider = Spider()
    headers = decoration.GetHeaders()
    for index in [0, 25]:
        url = 'https://movie.douban.com/top250?start=%d&filter=' % index
        print(url)
        text = spider.CaptureEx(url, headers)
        print(text)

def TestDangDangBeautifulSoup():
    root = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-'
    spider = Spider()
    parse = Parse()
    for page in range(1, 2):
        url = root + str(page)
        html = spider.Capture(url)
        ret = parse.HandleForDouBanByBS4(html)
        print(ret)
        

def TestDangDangRe():
    root = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-'
    spider = Spider()
    parse = Parse()
    for page in range(1,2):
        url = root + str(page)
        html = spider.Capture(url)
        res = parse.HandleForDouBanByRe(html)
        print(res)


def main()->int:
    #TestDangDang()
    #TestDangDangBeautifulSoup()
    TestDouBanByHeader()
    return 0


if __name__ == '__main__':
    main()