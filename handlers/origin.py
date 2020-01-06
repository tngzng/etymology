from handlers.base import BaseHandler
from models.word import get_origins


class OriginHandler(BaseHandler):
    def post(self):
        # TODO add validator for required arguments
        word = self.args['word']
        language_code = self.args['language_code']
        data = {'results': get_origins(word, language_code)}
        self.api_response(data)
