"""
spider interface
"""

import xmlrpc.client
from SpiderComponent.SpiderHandler import SpiderHandler
from LogComponent.LogMember import g_main_log


class Spider(object):
    def __init__(self):
        self.remoteHandler: xmlrpc.client.ServerProxy = None
        self.handler: SpiderHandler = None


    def Crawl(self, url: str)->bool:
        if self.remoteHandler:
            return self.remoteHandler.Crawl(url)
        elif self.handler:
            return self.handler.Crawl(url)

    
    def SetHandler(self, **args):
        if args.get('remote', None):
            g_main_log.info('connect to %s' % args['remote'])
            self.remoteHandler = xmlrpc.client.ServerProxy('http://%s/' % args['remote'])
        elif args.get('local', None):
            self.handler = args['local']
