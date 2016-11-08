from handlers.base_handler import BaseHandler
from tornado import gen
from tornado.httpclient import AsyncHTTPClient
from html.parser import HTMLParser
import json


def meta_to_dict(meta):
    result = dict()

    for pair in meta:
        key, value = pair

        print(key.split(':', 1))
        dict_key, dict_sub_key = key.split(':', 1)

        if dict_key in result:
            sub_dict = result[dict_key]
            sub_dict[dict_sub_key] = value
        else:
            result[dict_key] = dict()
            result[dict_key][dict_sub_key] = value
    return result


class MetaParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.meta = []

    def handle_starttag(self, tag, attrs):
        property = None
        content = None

        if tag == 'meta':
            for attr in attrs:
                type, value = attr
                if type == 'property':
                    property = value
                if type == 'content':
                    content = value

            if property is not None and content is not None:
                self.meta.append((property, content))

    def get_meta(self):
        return self.meta


class UrlHandler(BaseHandler):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)

    @gen.coroutine
    def post(self):
        self.prepare()
        url = self.json_args['url']
        http_client = AsyncHTTPClient()
        response = yield http_client.fetch(url)
        text_response = response.buffer.getvalue().decode('utf-8')

        parser = MetaParser()
        parser.feed(text_response)

        self.write(json.dumps(meta_to_dict(parser.get_meta())))

    def options(self, *args, **kwargs):
        pass