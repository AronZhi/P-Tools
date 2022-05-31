import json
from tornado.web import RequestHandler


class Handler(RequestHandler):
    def parseRequest(self):
        data = dict()        
        if self.request.headers.get('Content-Type') == 'application/json':
            data = json.loads(self.request.body.decode())
        else:
            for key in self.request.arguments:
                data[key] = self.get_argument(key)
        return data
    
    def sendJson(self,
                   comment,
                   **kwargs):
        ret = dict()
        ret.clear()
        ret['comment'] = comment
        if len(kwargs) > 0:
            ret.update(kwargs)
        self.set_header()
        self.write(json.dumps(ret))
        