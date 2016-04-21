#!/usr/bin/env python3
import tornado.ioloop
import tornado.web

from routes import routes


def make_app():
    return tornado.web.Application(routes, autoreload=True, debug=True)


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("The server is running on http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()
