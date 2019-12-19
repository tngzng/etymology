import logging

import tornado.httpserver
from tornado.ioloop import IOLoop
import tornado.options
import tornado.web

# import handlers.origin
import handlers.health


class Application(tornado.web.Application):
    def __init__(self):
        app_handlers = [
            (r'^/health$', handlers.health.HealthHandler),
            # (r'^/origin/(\S+)/(\S+)?$', handlers.origin.OriginHandler),
        ]
        super(Application, self).__init__(app_handlers)


if __name__ == '__main__':
    tornado.options.parse_command_line()

    port = 4000
    logging.info(f'listening on port {port}')

    http_server = tornado.httpserver.HTTPServer(request_callback=Application(), xheaders=True)
    http_server.listen(port)

    IOLoop.instance().start()