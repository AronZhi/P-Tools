from SpiderBase import *
import json
class StockHolderSpider(SpiderBase):
    def __init__(self):
        SpiderBase.__init__(self)


    def HandleStockHoldersHtml(self, html):
        sdltgdText = re.findall('var sdltgdData = \[.*\]', html)
        if sdltgdText:
            text = sdltgdText[0][17:]
            data = '{"sdltgd":' + text + '}'
            sdltgdJson = json.loads(data)
            print(sdltgdJson)


    def Crawl(self):
        code = 600598
        html = self.GetHtml('http://data.eastmoney.com/stockdata/%d.html' % code)
        if html:
            self.HandleStockHoldersHtml(html)
        else:
            print(self.GetLastError())
        