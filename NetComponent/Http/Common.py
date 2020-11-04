import psutil
import sys
import asyncio

def HandleAsyncioError():
    """
    处理python3.7及以上版本tornado使用asyncio抛出NotImplementedError异常
    """
    if psutil.WINDOWS and sys.version_info >= (3,7):
        import asyncio
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())