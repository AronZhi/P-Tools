import asyncio
import json
import tornado.web
import tornado.ioloop

class Handler(tornado.web.RequestHandler):
    def ParseRequest(self):
        data = dict()        
        if self.request.headers.get('Content-Type') == 'application/json':
            data = json.loads(self.request.body.decode())
        else:
            for key in self.request.arguments:
                data[key] = self.get_argument(key)
        return data
    
    def StopServer(self):
        tornado.ioloop.IOLoop.instance().stop()
        