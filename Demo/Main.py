from NetComponent.Http.UrlRequest import *
from Spider import Spider

def Main():
    lianJiaSpider = Spider()
    lianJiaSpider.UpdateSession(headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0'})
    for i in range(2):
        urlReq = UrlRequest()
        urlReq.action = UrlAction.Get
        if i == 0:
            urlReq.url = 'https://hz.lianjia.com/ershoufang/co32/'
        else:
            urlReq.url = 'https://hz.lianjia.com/ershoufang/pg%dco32/' % (i+1)
        lianJiaSpider.AddAsyncRequest(urlReq)
    lianJiaSpider.AsyncRunRequest()

if __name__ == '__main__':
    Main()