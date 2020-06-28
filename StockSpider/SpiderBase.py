import requests
import sys
import re
import bs4

class SpiderBase(object):
    def __init__(self):
        self.__last_error = ''
        self.__headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
        self.__proxies = {}

    
    def SetHeaders(self, headers: dict):
        if headers and len(headers) > 0:
            self.__headers = headers
    

    def SetProxies(self, proxies: dict):
        if proxies and len(proxies) > 0:
            self.__proxies = proxies

    
    def GetLastError(self)->str:
        return self.__last_error

    
    def HandleResponse(self, response):
        if response is None:
            return
        
        if response.status_code == 200:
            response.encoding = response.apparent_encoding
            self.__last_error = ''
            return response.text
        else:
            self.__last_error = 'crawl response %d' % response.status_code
            return ''


    def GetHtml(self, url: str)->str:
        try:
            html = ''
            if len(self.__proxies) > 0:
                response = requests.get(url, headers = self.__headers, proxies = self.__proxies)
                html = self.HandleResponse(response)
            else:
                response = requests.get(url, headers = self.__headers)
                html = self.HandleResponse(response)
            return html

        except requests.exceptions():
            self.__last_error = 'crawl request fail'
            return ''
        except:
            self.__last_error = 'crawl system fail: %s' % sys.exc_info()[0]
            return ''