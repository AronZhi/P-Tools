class ReqObj(object):
    def __init__(self, url, method="GET", body=None, headers={}, resHandle = None) -> None:
        self.url = url
        self.method = method
        self.body = body
        self.headers = headers
        self.resHandle = resHandle if resHandle else lambda res:print(self.url, " response: ", res.code)