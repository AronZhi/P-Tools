import tornado.web
import tornado.httpserver
import tornado.ioloop

from .Common import *

class Server(object):
    def Run(self, port: int, protocol: list):
        HandleAsyncioError()
        app = tornado.web.Application(protocol)
        httpServer = tornado.httpserver.HTTPServer(app)
        httpServer.listen(port)
        tornado.ioloop.IOLoop.instance().start()