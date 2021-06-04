import json
from functools import wraps

class Mark(object):
    @classmethod
    def handleFuncInfo(cls, jsonData):
        print(jsonData)

    @classmethod
    def MarkFuncInfo(cls, func):
        @wraps(func)
        def fetchInfo(*args, **kwargs):
            data = {"module": func.__module__, "func": func.__name__, "kwargs": kwargs, "args": args}
            jsonData = json.dumps(data)
            cls.handleFuncInfo(jsonData)
            ret = func(*args, **kwargs)
            return ret
        return fetchInfo
    
    @classmethod
    def handleFuncProcess(cls, data):
        print(data)
    
    @classmethod
    def MarkFuncProcess(cls, func):
        @wraps(func)
        def recordProcess(*args, **kwargs):
            cls.handleFuncProcess(func.__name__ + ' start')
            ret = func(*args, **kwargs)
            cls.handleFuncProcess(func.__name__ + ' end')
            return ret
        return recordProcess

"""
@Mark.MarkFuncProcess
@Mark.MarkFuncInfo
def test1(a, b, c, *args):
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(args)
    #print(kwargs)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

@Mark.MarkFuncProcess
@Mark.MarkFuncInfo
def test2(*args, a, b, c):
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(args)
    #print(kwargs)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

test1(1, 2, 3, 1, 2, 1)
#test1(1, 2, 3, a=1, b=2, c=1)
#test1(a=1, b=2, c=3, 1, 2, 1)
test2(1, 2, 3, a=1, b=2, c=1)
#test2(1, 2, 3, 1, 2, 1)
"""