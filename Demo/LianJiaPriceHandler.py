from bs4 import BeautifulSoup

class LianJiaPriceHandler(object):
    def ParseHtml(self, html):
        soup = BeautifulSoup(html, features='html.parser')
        house_list = soup.find_all(class_ = 'info clear')
        for houseInfo in house_list:
            print(houseInfo)