from handlers.base_handler import BaseHandler


class MainHandler(BaseHandler):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)

    def get(self):
        self.write("Hello, world")
