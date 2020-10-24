import logging
from functools import wraps

output = None

def outPutSoruce(writer:logging.Logger = None):
    output = writer

def Printf(text):
    if output:
        output.info(text)
    else:
        print(text)

def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        Printf(func.__name__ + ' start')
        ret = func(*args, **kwargs)
        Printf(func.__name__ + ' end')
        return ret
    return with_logging
        