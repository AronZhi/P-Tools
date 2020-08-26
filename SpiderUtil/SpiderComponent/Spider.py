import multiprocessing
import requests
import time
import xmlrpc.client
from MsgComponent.MsgType import msg_type
from MsgComponent.Msg import Msg
from SpiderComponent.SpiderParam import SpiderParam
from LogComponent.LogMember import g_main_log


class Spider(object):
    def __init__(self):
        self.param = SpiderParam()
        self.partners = dict()

    
    def HandleMsg(self, url, msg: Msg):
        """
        web page parse function
        """
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

    
    def _Crawl(self, url)->bool:
        msg = self._GetHtml(url)
        return self.HandleMsg(url, msg)


    def Crawl(self, url: str, partnerIP: str)->bool:
        if self.partners.get(partnerIP, None):
            self.partners[partnerIP]._Crawl(url)
        else:
            return self._Crawl(url)

    
    def GetPartner(self, remote: str):
        g_main_log.info('connect to %s' % remote)
        partner = xmlrpc.client.ServerProxy('http://%s/' % host, verbose=True)
        self.partners[remote] = partner
