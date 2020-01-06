import json

from handlers.base import BaseHandler
from validators.descendant import DescendantValidator
from pydantic import ValidationError
from models.word import get_descendants


class DescendantHandler(BaseHandler):
    def post(self):
        try:
            args = DescendantValidator(**self.args)
        except ValidationError as e:
            error_dict = json.loads(e.json())
            self.api_response(error_dict, code=400)
            return

        data = {'results': get_descendants(args.word, args.language_code)}
        self.api_response(data)
