import re
import bs4

class Parse(object):
    def HandleForDouBanByRe(self, html: str):
        pattern = re.compile('<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span\sclass="price_n">&yen;(.*?)</span>.*?</li>',re.S)
        items = re.findall(pattern,html)
        res = []
        for item in items:
            element = {
                'range': item[0],'iamge': item[1],'title': item[2],'recommend': item[3],
                'author': item[4],'times': item[5],'price': item[6]
                }
            res.append(element)
        
        return res

    def HandleForDouBanByBS4(self, html: str):
        soup = bs4.BeautifulSoup(html, features="html.parser")
        list = soup.find(class_ = 'bang_list clearfix bang_list_mode').find_all('li')
        ret = []
        for item in list:
            titleInfo = item.find(class_ = 'name')
            title = titleInfo.find('a').get('title')
            ret.append(title)
        return ret