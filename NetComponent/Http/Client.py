import asyncio
import requests
from .UrlRequest import *

class Client(object):
    def __init__(self):
        self.session = requests.Session()
        self.asyncRequests = list()
    
    def UpdateSession(self, **kwargs):
        if kwargs.get('headers', None):
            self.session.headers.update(kwargs['headers'])
    
    def HandleHtml(self, html):
        print(html)
        return False
    
    def _OnAsyncResponse(self, task: asyncio.Task):
        html = task.result()
        return self.HandleHtml(html)
    
    def _HandleRequest(self, urlRequest: UrlRequest):
        try:
            if urlRequest.action == UrlAction.Get:
                response = self.session.get(urlRequest.url)
            elif urlRequest.action == UrlAction.Post:
                response = self.session.post(urlRequest.url, data=urlRequest.data)
            if response.status_code == 200:
                return response.text
            else:
                return 'fail with code %d' % response.status_code
        except Exception as e:
            return 'error: %s' % e
    
    async def _Task(self, urlRequest: UrlRequest):
        return self._HandleRequest(urlRequest)
    
    async def _main(self):
        loop = asyncio.get_running_loop()
        for request in self.asyncRequests:
            task = loop.create_task(self._Task(request))
            task.add_done_callback(self._OnAsyncResponse)
            await task
    
    def AddAsyncRequest(self, urlRequest: UrlRequest):
        self.asyncRequests.append(urlRequest)
    
    def AsyncRunRequest(self):
        asyncio.run(self._main())
    
    def Get(self, url):
        urlReq = UrlRequest()
        urlReq.action = UrlAction.Get
        urlReq.url = url
        html = self._HandleRequest(urlReq)
        self.HandleHtml(html)
    
    def Post(self, url, data):
        urlReq = UrlRequest()
        urlReq.action = UrlAction.Post
        urlReq.url = url
        urlReq.data = data
        html = self._HandleRequest(urlReq)
        self.HandleHtml(html)

    