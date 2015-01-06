import web

from config import Config
from openttd.stats_query import StatsQuery
from context import Context


urls = (
    '/stats', 'Stats',
    '/admin', 'admin'
)


#taken from http://stackoverflow.com/a/14445064/291114
class PoxyWebApp(web.application):
    def run(self, port=8080, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))


class ServerController:
    def __init__(self, startup):
        self.startup = startup

        self.context = Context()
        self.context.set_config(Config(self.startup['config_path']))
        self.context.set_openttd(StatsQuery(self.context.get_config().instance))

    if __name__ == "__main__":
        app = MyApplication(urls, globals())
        app.run(port=8888)

    def start_server(self):
        general = self.context.get_config().general

        app = PoxyWebApp(urls, globals())
        app.run(general.listen_port)
