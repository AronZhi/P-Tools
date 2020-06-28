from SpiderBase import *

class StockHolderSpider(SpiderBase):
    def __init__(self):
        SpiderBase.__init__(self)


    def HandleStockHoldersHtml(self, html):
        soup = bs4.BeautifulSoup(html, 'html.parser')
        lst = soup.find(class_ = 'm_table m_hl ggintro').find_all('a')
        for item in lst:
            if item.text == '点击查看':
                text = (item.get('onclick'))
                res = re.findall('\'.*\'', text)
                if res:
                    print(res[2])


    def Crawl(self):
        html = self.GetHtml('http://basic.10jqka.com.cn/000651/holder.html')
        if html:
            self.HandleStockHoldersHtml(html)
        else:
            print(self.GetLastError())
        