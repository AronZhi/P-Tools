import logging
import json
from functools import wraps

PrintTool = None

def SetPrintTool(writer:logging.Logger = None):
    global PrintTool
    PrintTool = writer

def Printf(text):
    global PrintTool
    if PrintTool:
        PrintTool.info(text)
    else:
        print(text)

def LogInterface(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        Printf(func.__name__ + ' start')
        ret = func(*args, **kwargs)
        Printf(func.__name__ + ' end')
        return ret
    return with_logging

def FormatFuncAsJson(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        data = {"func": func.__name__, "kwargs": kwargs}
        jsonData = json.dumps(data)
        print(jsonData)
        ret = func(*args, **kwargs)
        return ret
    return with_logging

"""
@FormatFuncAsJson
def test(test):
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(test)
    #print(kwargs)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

if __name__ == "__main__":
    from LogMember import g_main_log
    SetPrintTool(g_main_log)
    test(test=1)
"""