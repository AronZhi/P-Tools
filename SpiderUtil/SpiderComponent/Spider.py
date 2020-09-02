"""
spider interface
"""

import xmlrpc.client
from SpiderComponent.PageCrawler import PageCrawler
from SpiderComponent.PageHandler import PageHandler
from LogComponent.LogMember import g_main_log


class SpiderCtrl(object):
    def __init__(self, handler: PageHandler, crawler: PageCrawler = None):
        self.handler = handler
        if crawler:
            self.crawler = crawler
        else:
            self.crawler = PageCrawler()

    
    def Crawl(self, url):
        page = self.crawler.FetchPage(url)
        return self.handler.HandlePage(page)


class Spider(object):
    def __init__(self):
        self.remoteCtrl: xmlrpc.client.ServerProxy = None
        self.localCtrl: SpiderCtrl = None


    def Crawl(self, url: str)->bool:
        g_main_log.info('start crawl url:%s' % url)
        if self.remoteCtrl:
            return self.remoteCtrl.Crawl(url)
        elif self.localCtrl:
            return self.localCtrl.Crawl(url)

    
    def SetCtrl(self, **args):
        if args.get('remote', None):
            g_main_log.info('connect to %s' % args['remote'])
            self.remoteCtrl = xmlrpc.client.ServerProxy('http://%s/' % args['remote'])
        elif args.get('local', None):
            self.localCtrl = args['local']
        elif args.get('page_handler', None):
            self.localCtrl = SpiderCtrl(args['page_handler'])
