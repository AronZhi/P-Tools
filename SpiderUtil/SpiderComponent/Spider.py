import multiprocessing
import requests
import time
from MsgComponent.MsgType import msg_type
from MsgComponent.Msg import Msg
from SpiderComponent.SpiderParam import SpiderParam


class Spider(object):
    def __init__(self):
        self.param = SpiderParam()

    
    def HandleMsg(self, url, msg: Msg):
        return True


    def _GetHtml(self, url: str):
        ret = Msg()
        try:
            response = requests.get(url, headers = self.param.headers, proxies = self.param.proxies, timeout = self.param.timeout)
            if response.status_code == 200:
                ret.type = msg_type.success
                response.encoding = response.apparent_encoding
                ret.data = response.text
            else:
                ret.type = msg_type.fail
                ret.data = 'response return %d' % response.status_code

        except requests.exceptions.RequestException as httpError:
            ret.type = msg_type.error
            ret.data = 'request error occur: %s' % str(httpError) 
        except Exception as systemError:
            ret.type = msg_type.systemError
            ret.data = 'system error occur: %s' % str(systemError)
        
        return ret


    def Crawl(self, url: str)->Msg:
        msg = self._GetHtml(url)
        return self.HandleMsg(url, msg)
