"""
spider interface
"""

import xmlrpc.client
from SpiderComponent.SpiderHandler import SpiderHandler
from LogComponent.LogMember import g_main_log


class Spider(object):
    def __init__(self):
        self.partner: xmlrpc.client.ServerProxy = None
        self.handler: SpiderHandler = None


    def Crawl(self, url: str)->bool:
        if self.partner:
            return self.partner.Crawl(url)
        elif self.handler:
            return self.handler.Crawl(url)

    
    def SetPartner(self, remote: str):
        g_main_log.info('connect to %s' % remote)
        self.partner = xmlrpc.client.ServerProxy('http://%s/' % remote)

    
    def SetHandler(self, handler: : SpiderHandler):
        self.handler = handler
