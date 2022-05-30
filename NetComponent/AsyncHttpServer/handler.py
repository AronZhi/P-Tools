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
    
    def sendResult(self,
                   comment,
                   ret = {}):
        ret['comment'] = comment
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps(ret))
        