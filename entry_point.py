import tornado.web
import tornado.ioloop
from handlers.main_handler import MainHandler
from handlers.url_handler import UrlHandler


def run_app(port):
    app = tornado.web.Application([(r"/", MainHandler),
                                   (r"/url", UrlHandler)])
    app.listen(port=port)
    tornado.ioloop.IOLoop.current().start()

run_app(8888)