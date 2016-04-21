from handlers import HomePage
import settings
from tornado import web

routes = [
    (r"/", HomePage),
    (r"/static/(.*)", web.StaticFileHandler, {"path": settings.STATIC_PATH}),
]
