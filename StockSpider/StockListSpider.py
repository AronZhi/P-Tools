import bs4
import sys

sys.path.append('C:\WorkSpace\Test\Spider\Spider')
from Spider import Spider
from MsgType import msg_type
from Msg import Msg


class StockListSpider(Spider):
    def __init__(self):
        Spider.__init__(self)
        self.__shMainStocks = {}
        self.__szMainStocks = {}
        self.__cyStocks = {}
        self.__kcStocks = {}

    
    def HandleStockListHtml(self, html):
        soup = bs4.BeautifulSoup(html, 'html.parser')
        lst = soup.find(class_ = 'quotebody').find_all('li')
        for item in lst:
            text = item.text
            num = re.findall('\d{6}', text)
            code = int(num[0])
            name = text[0:text.find('(')]
            if code < 31000:
                self.__szMainStocks[num[0]] = name
            elif code > 300000 and code < 400000:
                self.__cyStocks[num[0]] = name
            elif code >= 600000 and code < 688000:
                self.__shMainStocks[num[0]] = name
            elif code > 688000 and code < 700000:
                self.__kcStocks[num[0]] = name


    def HandleMsg(self, url, msg: Msg):
        if msg.type == msg_type.success:
            self.HandleStockListHtml(msg.data)
            return True
        else:
            print(msg.data)
        return False


    def Start(self):
        msg = self.Crawl('http://quote.eastmoney.com/stock_list.html')


    def GetSHMainStocks(self):
        return self.__shMainStocks


    def GetKCStocks(self):
        return self.__kcStocks


    def GetSZMainStocks(self):
        return self.__szMainStocks


    def GetCYStocks(self):
        return self.__cyStocks