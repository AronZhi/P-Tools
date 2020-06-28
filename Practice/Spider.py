
import requests

class Spider(object):
    def CaptureEx(self, url: str, header):
        try:
            response = requests.get(url, headers = header)
            if response.status_code == 200:
                return response.text
            else:
                return 'capture %s fail, ret:%d' % (url, response.status_code)
        except requests.exceptions:
            return 'capture %s err' % url

    def Capture(self, url: str):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
            else:
                return 'capture %s fail, ret:%d' % (url, response.status_code)
        except requests.exceptions:
            return 'capture %s err' % url