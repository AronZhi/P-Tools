import requests
import csv

class SpiderBase(object):
    def __init__(self):
        self.__headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
        self.__proxies= {}


    def Create(self, headers: dict, proxies: dict = None):
        self.__headers = headers
        if proxies:
            self.__proxies = proxies


    def SetHeaders(self, headers):
        self.__headers = headers


    def SetProxies(self, proxies):
        self.__proxies = proxies


    def GetHtml(self, url):
        try:
            if len(self.__proxies) > 0:
                res = requests.get(url, headers = self.__headers, proxies = self.__proxies)
            else:
                res = requests.get(url, headers = self.__headers)
            
            if res.status_code == 200:
                return res.text
            else:
                return 'get html from %s return %d' % (url, res.status_code)

        except requests.exceptions:
            return 'get html from %s request error occur' % url

    