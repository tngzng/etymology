import json

import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    """Wrapper for handler abstractions"""
    def prepare(self):
        if self.request.headers['Content-Type'] == 'application/json':
            self.args = json.loads(self.request.body)

    def api_response(self, data, code=200):
        self.set_status(code)
        if isinstance(data, dict):
            self.set_header('Content-Type', 'application/json')

        if not 200 <= code < 300:
            data = {'message': data}
        if not isinstance(data, str):
            data = json.dumps(data)

        self.finish(data)
