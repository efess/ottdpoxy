import web
from context import Context
from model.request import Request
from model.response import Response


class stats:

    def GET(self):
        return "<p style='font-family: \"Lucida Console\", Monaco, monospace'>OTTDPoxy: Get is not supported.</p>"

    def POST(self):
        config = Context.get_context().get_config().stats
        if not config.web_host_access is "":
            web.header('Access-Control-Allow-Origin', config.web_host_access)

        if not config.enabled:
            response = Response()
            response.status = 2
            response.error = 'Stats module is not enabled'
            return response.serialize()

        data = web.data()
        request = Request(data)

        if not self.__is_authenticated(config, request):
            response = Response()
            response.status = 2
            response.error = 'You are not authenticated to access this resource'
            return response.serialize()

        if not request.payload or not 'action' in request.payload:
            return

        action = request.payload['action']

        if action == 'get':
            return self.__get_stats()

    def __is_authenticated(self, config, request):
        if config.allow_public:
            return True

        if config.password != '' and config.password == request.password:
            return True

        return False

    def __get_stats(self):

        response = Response()

        try:
            stats = Context.get_context().get_openttd().do_query()
            if stats is None:
                response.status = 2
                response.error = "No response from server"
            else:
                response.payload = {'stats':
                                        {
                                            'company_info': stats.company_info,
                                            'game_info': stats.game_info,
                                            'client_info': stats.client_info,

                                        }
                                    }
                response.status = 0
        except Exception as ex:
            response.status = 1
            response.error = "Error polling server"

        return response.serialize()
