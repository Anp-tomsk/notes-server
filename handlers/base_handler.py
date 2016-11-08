import tornado.web
import tornado.escape


class BaseHandler(tornado.web.RequestHandler):
    SUPPORTED_METHODS = ("CONNECT", "GET", "HEAD", "POST", "DELETE", "PATCH", "PUT", "OPTIONS")

    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.json_args = None

    def prepare(self):
        if "Content-Type" in self.request.headers:
            if self.request.headers["Content-Type"].startswith("application/json"):
                self.json_args = tornado.escape.json_decode(self.request.body)

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def data_received(self, chunk):
        pass
