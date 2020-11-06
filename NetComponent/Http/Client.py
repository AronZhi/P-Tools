import asyncio
import requests

class Client(object):
    def __init__(self):
        self.session = requests.Session()
    
    def updateSession(self, **kwargs):
        if kwargs.get('headers', None):
            self.session.headers.update(kwargs['headers'])
    
    def HandleHtml(self, html):
        print(html)
    
    def _InitFuture(self, loop)->asyncio.Future:
        future = loop.create_future()
        def callback(future):
            self.HandleHtml(future.result())
        future.add_done_callback(callback)
        return future
    
    async def _Work(self, future, workfunc):
        try:
            response = workfunc()
            if response.status_code == 200:
                future.set_result(response.text)
            else:
                future.set_result('fail with code %d' % response.status_code)
        except Exception as e:
            future.set_result('error: %s' % e)
    
    async def _Get(self, url):
        loop = asyncio.get_running_loop()
        future = self._InitFuture(loop)
        task = loop.create_task(self._Work(future, lambda : self.session.get(url)))
        await task
    
    async def _Post(self, url, data):
        loop = asyncio.get_running_loop()
        future = self._InitFuture(loop)
        task = loop.create_task(self._Work(future, lambda : self.session.post(url, data=data)))
        await task
    
    def Get(self, url):
        asyncio.run(self._Get(url))
    
    def Post(self, url, data):
        asyncio.run(self._Post(url, data))
    