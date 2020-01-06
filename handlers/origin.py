import json

from handlers.base import BaseHandler
from validators.origin import OriginValidator
from pydantic import ValidationError
from models.word import get_origins


class OriginHandler(BaseHandler):
    def post(self):
        try:
            args = OriginValidator(**self.args)
        except ValidationError as e:
            error_dict = json.loads(e.json())
            self.api_response(error_dict, code=400)
            return

        data = {'results': get_origins(args.word, args.language_code)}
        self.api_response(data)
