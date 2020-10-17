import requests
import sys
from LogComponent.LogMember import g_main_log

user_agent = {'windows': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv 11.0) like Gecko',
    'mac': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) ' \
        'AppleWebKit/537.36 (KHTML, like Gecko) ' \
        'Chrome/75.0.3770.100 Safari/537.36'}

time_out = 30


class PageCrawler(object):
    def __init__(self):
        self.session = requests.Session()
        if sys.platform == 'darwin':
            self.session.headers.update({'User-Agent': user_agent['mac']})
        else:
            self.session.headers.update({'User-Agent': user_agent['windows']})


    def FetchPage(self, url):
        try:
            response = self.session.get(url, timeout = time_out)
            if response.status_code == 200:
                return response.text
            else:
                g_main_log.warn('fetch page fail, status code:%d' % response.status_code)
                return None
        except requests.exceptions.RequestException as httpError:
            g_main_log.warn('request error occur: %s' % str(httpError))
        except Exception as systemError:
            g_main_log.warn('system error occur: %s' % str(systemError))
        return None