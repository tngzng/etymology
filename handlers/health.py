from handlers.base import BaseHandler


class HealthHandler(BaseHandler):
    """Return 200 OK."""

    def get(self):
        self.api_response('OK')
