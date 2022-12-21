import asyncio
from aiohttp.client import ClientSession

class Client(object):
    def __init__(self, req_headers:dict = None):
        if req_headers is None:
            self._headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.5',
            'Host': 'xueqiu.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'
            }
        else:
            self._headers = req_headers

    async def get(self, url, *, data:dict=None, call_back_func = None, is_async_callback=False):
        """

        callback function template
        def call_back_func(task: asyncio.Task):
            html_text = task.result()

        """
        handle = lambda response : await call_back_func(response) if is_async_callback else call_back_func(response)
        async with ClientSession() as session:
            if data:
                async with session.get(url, headers=self._headers, params=data) as response:
                    await response.text()
                    handle(response.text())
            else:
                async with session.get(url, headers=self._headers) as response:
                    await response.text()
                    handle(response.text())
    
    async def post(self, url, *, data:dict=None, call_back_func = None, is_async_callback=False):
        """

        callback function template
        def call_back_func(task: asyncio.Task):
            html_text = task.result()
            
        """
        handle = lambda response : await call_back_func(response) if is_async_callback else call_back_func(response)
        async with ClientSession() as session:
            if data:
                async with session.post(url, headers=self._headers, params=data) as response:
                    await response.text()
                    handle(response.text())
            else:
                async with session.post(url, headers=self._headers) as response:
                    await response.text()
                    handle(response.text())