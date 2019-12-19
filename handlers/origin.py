from handlers.base import BaseHandler


class OriginHandler(BaseHandler):
    def get(self, language_code, word):
        self.api_response('OK')
