from bs4 import BeautifulSoup
from SpiderBase import *
import re

class LianjiaSpider(SpiderBase):
    def HandleHtml(self, html):
        """
        计算每平米均价
        """
        soup = BeautifulSoup(html, features='html.parser')
        houseList = soup.find(class_ = 'content__list').find_all(class_ = 'content__list--item--main')

        head = ['locate', 'rent', 'area']
        with open('data.csv', 'a') as csvfile:
            f = csv.DictWriter(csvfile, fieldnames = head)
            f.writeheader()

            for houseInfo in houseList:
                areaStr = re.findall('[\d{1,}㎡]\d{1,}', houseInfo.find(class_='content__list--item--des').text)
                rentStr = houseInfo.find(class_ = 'content__list--item-price').find('em').text
                if areaStr and rentStr:
                    line = {'rent': rentStr, 'area': areaStr[0], 'locate': 'bingjiang'}
                    f.writerow(line)


    def Crawl(self):
        url = 'https://hz.lianjia.com/zufang/binjiang/pg2/#contentList'
        html = self.GetHtml(url)
        self.HandleHtml(html)