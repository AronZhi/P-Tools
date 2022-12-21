import asyncio
from aiohttp.client import ClientSession

class Crawler(object):
    def __init__(self, event_loop):
        self._headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.5',
            'Host': 'xueqiu.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'
        }
        assert event_loop
        self._event_loop = event_loop

    async def _get(self, session, url):
        async with session.get(url, headers=self._headers) as response:
            return await response.text()

    async def get(self, *, call_back_func, url='', urls=[]):
        """
        :param urls: list of url
        :param call_back_func: handle one html, format is async func(task: asyncio.Task)
        :return: None

        callback function template
        def call_back_func(task: asyncio.Task):
            html_text = task.result()
            
        """
        task_lst = []
        async with ClientSession() as session:
            if url:
                urls.append(url)
            for url in urls:
                task = self._event_loop.create_task(self._get(session, url))
                task.add_done_callback(call_back_func)
                task_lst.append(task)
            for async_task in task_lst:
                await async_task