import logging
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
        