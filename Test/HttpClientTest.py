from NetComponent.Http.Client import *
from NetComponent.Http.UrlRequest import *

def stop():
    client = Client()
    client.Get('http://10.224.84.217:8888/?command=stop')

def get():
    client = Client()
    client.Get('http://10.224.84.217:8888/?command=test')

def post():
    client = Client()
    dataDict = dict()
    dataDict['echo'] = 'test'
    client.Post('http://10.224.84.217:8888/', dataDict)

def headers():
    client = Client()
    client.updateSession(headers = {"Content-Type": "application/json"})
    msg = '{"client_version" : "40.12.0.159", "conf_id" : "176421468506168610", "cpu" : {"core" : 8, "freq" : "2.112000"}}'
    content = '{"echo": ' + msg + '}'
    client.Post('http://10.224.84.217:8888/', content.encode())

def request():
    client = Client()
    urlrequest1 = UrlRequest()
    urlrequest1.action = UrlAction.Get
    urlrequest1.url = 'http://10.224.84.217:8888/?command=test'
    client.AddAsyncRequest(urlrequest1)
    urlrequest2 = UrlRequest()
    dataDict = dict()
    dataDict['echo'] = 'show hello'
    urlrequest2.action = UrlAction.Post
    urlrequest2.url = 'http://10.224.84.217:8888/'
    urlrequest2.data = {'echo':'hello test'}
    client.AddAsyncRequest(urlrequest2)
    client.AsyncRunRequest()

if __name__ == '__main__':
    request()