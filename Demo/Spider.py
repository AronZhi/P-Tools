from NetComponent.Http.Client import Client
from LogComponent.LogMember import *
from LianJiaPriceHandler import LianJiaPriceHandler

class Spider(Client):
    def HandleHtml(self, html):
        handler = LianJiaPriceHandler()
        handler.ParseHtml(html)