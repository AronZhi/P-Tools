import json
from functools import wraps

def traceFunction(func):
    @wraps(func)
    def traceFunctionWrapper(*args, **kwargs):
        trace = dict()
        trace['module'] = func.__module__
        trace['func'] = func.__name__
        trace['args'] = args
        trace['kwargs'] = kwargs
        try:
            ret = func(*args, **kwargs)
            #trace['result'] = ret
            return ret
        except Exception as e:
            trace['error'] = str(e)
        finally:
            print(json.dumps(trace))
    return traceFunctionWrapper

"""
@traceFunction
def div(a, b):
    return a/b

if __name__ == "__main__":
    div(1, 0)
    div(1, 2)
"""