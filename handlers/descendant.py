from handlers.base import BaseHandler
from models.word import get_descendants


class DescendantHandler(BaseHandler):
    def get(self, language_code, word):
        data = {'results': get_descendants(word, language_code)}
        self.api_response(data)
