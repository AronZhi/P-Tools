from LianjiaSpider import *
from SpiderComponent.Spider import Spider
from LogComponent.LogMember import g_main_log


def main()->int:
    lianjiaHandler = LianjiaHandler()
    spider = Spider()
    spider.SetCtrl(page_handler = lianjiaHandler)

    for index in range(1,100):
        url = 'https://hz.lianjia.com/zufang/pg%drco11/#contentList' % index
        if index == 1:
            url = 'https://hz.lianjia.com/zufang/rco11/#contentList'
        g_main_log.info('start crawl %s' % url)
        spider.Crawl(url)
        time.sleep(1)
    return 0 

if __name__ == '__main__':
    main()
    