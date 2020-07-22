import json
import sys

from SpiderComponent.Spider import Spider
from MsgComponent.MsgType import msg_type
from MsgComponent.Msg import Msg


class StockHolderSpider(Spider):
    def __init__(self):
        Spider.__init__(self)


    def HandleStockHoldersHtml(self, html):
        sdltgdText = re.findall('var sdltgdData = \[.*\]', html)
        if sdltgdText:
            text = sdltgdText[0][17:]
            data = '{"sdltgd":' + text + '}'
            sdltgdJson = json.loads(data)
            print(sdltgdJson)
    

    def HandleMsg(self, url, msg: Msg):
        if msg.type == msg_type.success:
            self.HandleStockHoldersHtml(msg.data)
            return True
        else:
            print(msg.data)
        return False

    
    def Start(self):
        code = '002463'
        self.Crawl('http://data.eastmoney.com/stockdata/%s.html' % code)