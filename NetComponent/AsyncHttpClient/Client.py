import asyncio
import tornado.ioloop
import tornado.httpclient
from ReqObj import ReqObj

class Client(object):
    def __init__(self):
        """
        windows环境python3.7及以上版本tornado使用asyncio抛出NotImplementedError异常，
        试用前需要以下处理
        if psutil.WINDOWS and sys.version_info >= (3,7):
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        """
        self.client: tornado.httpclient.AsyncHTTPClient = tornado.httpclient.AsyncHTTPClient()
        self.reqList = list()
        self.ioLoop = tornado.ioloop.IOLoop.current()
    
    def __del__(self):
        self.client.close()
    
    def AddTask(self, req: ReqObj):
        self.reqList.append(req)
        return
    
    async def __Request(self, req: ReqObj):
        res = await self.client.fetch(req.url, method=req.method, body=req.body, headers=req.headers)
        if req.resHandle:
            req.resHandle(res)
    
    async def __Run(self):
        tasklist = []
        for req in self.reqList:
            task = asyncio.create_task(self.__Request(req))
            tasklist.append(task)
        self.reqList.clear()
        for task in tasklist:
            await task
    
    def DoUntilComplete(self):
        self.ioLoop.run_sync(self.__Run)

"""
if __name__ == "__main__":
    import platform
    if(platform.system() =="Windows"):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    client = Client()
    client.AddTask(ReqObj(url = "https://blog.csdn.net/forever_008/article/details/103495708"))
    client.AddTask(ReqObj(url = "https://www.baidu.com/index.php?tn=monline_3_dg"))
    client.DoUntilComplete()
"""