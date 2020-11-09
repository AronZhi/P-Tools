import asyncio
import requests

class Client(object):
    def __init__(self):
        self.session = requests.Session()
    
    def updateSession(self, **kwargs):
        if kwargs.get('headers', None):
            self.session.headers.update(kwargs['headers'])
    
    def OnResponse(self, task: asyncio.Task):
        html = task.result()
        print(html)
    
    async def _Work(self, workfunc):
        try:
            response = workfunc()
            if response.status_code == 200:
                return response.text
            else:
                return 'fail with code %d' % response.status_code
        except Exception as e:
            return 'error: %s' % e
    
    async def _Get(self, url):
        loop = asyncio.get_running_loop()
        task = loop.create_task(self._Work(lambda : self.session.get(url)))
        task.add_done_callback(self.OnResponse)
        await task
    
    async def _Post(self, url, data):
        loop = asyncio.get_running_loop()
        task = loop.create_task(self._Work(lambda : self.session.post(url, data=data)))
        task.add_done_callback(self.OnResponse)
        await task

    def Get(self, url):
        asyncio.run(self._Get(url))
    
    def Post(self, url, data):
        asyncio.run(self._Post(url, data))

    