import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    """Wrapper for handler abstractions"""

    def api_response(self, data, code=200):
        self.set_status(code)
        self.set_header('Content-Type', 'application/json')

        if not 200 <= code < 300:
            response = {'message': data}
        else:
            response = data

        self.finish(response)
