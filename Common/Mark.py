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
            data = {"func": func.__name__, "kwargs": kwargs}
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
def test(test):
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(test)
    #print(kwargs)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

if __name__ == "__main__":
    test(test=1)
"""