from SpiderBase import *
import json
class StockHolderSpider(SpiderBase):
    def __init__(self):
        SpiderBase.__init__(self)


    def HandleStockHoldersHtml(self, html):
        sdltgdText = re.findall('var sdltgdData = \[.*\]', html)
        if sdltgdText:
            text = sdltgdText[0][16:-1]
            print(data)


    def Crawl(self):
        html = self.GetHtml('http://data.eastmoney.com/stockdata/600598.html')
        if html:
            self.HandleStockHoldersHtml(html)
        else:
            print(self.GetLastError())
        