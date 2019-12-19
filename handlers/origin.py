from handlers.base import BaseHandler
from models.word import get_origins


class OriginHandler(BaseHandler):
    def get(self, language_code, word):
        data = {'results': get_origins(word, language_code)}
        self.api_response(data)
