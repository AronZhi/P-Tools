class UrlAction(object):
    Get = 'get'
    Post = 'post'

class UrlRequest(object):
    def __init__(self):
        self.action: str = ''
        self.url: str = ''
        self.data = None