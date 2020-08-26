import asyncio

async def DoSomeWork(msg:str, waitTime:int):
    print('DoSomeWork start:', msg)
    await asyncio.sleep(waitTime) #挂起当前协程，去执行asyncio.sleep(waitTime) 协程
    print('DoSomeWork end')

def DoSomeWorkCallback(future):
    print('do some work callback')

async def DoSomeWork2(msg:str, waitTime:int):
    print('DoSomeWork2 start:', msg)
    await asyncio.sleep(waitTime)
    print('DoSomeWork2 start')

def DoSomeWork2Callback(future):
    print('do some work2 callback')

async def DoSomeWork3(msg:str, coroutine):
    print('DoSomeWork3 start:', msg)
    await coroutine
    print('DoSomeWork3 end')

async def DoSomeWork4(msg:str, coroutine):
    print('DoSomeWork4 start:', msg)
    await coroutine
    print('DoSomeWork4 end')

def Test1():
    eventLoop = asyncio.get_event_loop() #获取事件循环
    eventLoop.run_until_complete(asyncio.ensure_future(DoSomeWork('test', 5)))
    eventLoop.close() #关闭循环
    print('the end')

def Test2():
    eventLoop = asyncio.get_event_loop()
    future = asyncio.ensure_future(DoSomeWork('test', 2))
    future.add_done_callback(DoSomeWorkCallback) #增加回调函数
    eventLoop.run_until_complete(future)
    eventLoop.close()
    print('the end')

def Test3():
    evenLoop = asyncio.get_event_loop()
    futures = []
    future1 = asyncio.ensure_future(DoSomeWork('test1', 2))
    future1.add_done_callback(DoSomeWorkCallback)
    futures.append(future1)
    future2 = asyncio.ensure_future(DoSomeWork2('test2', 3))
    future2.add_done_callback(DoSomeWork2Callback)
    futures.append(future2)
    evenLoop.run_until_complete(asyncio.gather(*futures))
    evenLoop.close()
    print('the end')

def Test4():
    evenLoop = asyncio.get_event_loop()
    task1 = asyncio.ensure_future(DoSomeWork('test', 2))
    task2 = asyncio.ensure_future(DoSomeWork3('test3', task1))
    future = asyncio.ensure_future(DoSomeWork4('test4', task2))
    evenLoop.run_until_complete(future)
    print('the end')

if __name__ == '__main__':
    Test4()