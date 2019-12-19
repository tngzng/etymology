from handlers.base import BaseHandler


class DescendantHandler(BaseHandler):
    def get(self, language_code, word):
        self.api_response('OK')
