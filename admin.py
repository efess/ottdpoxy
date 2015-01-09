import base64
import web
import os
import glob
from context import Context
from model.request import Request
from model.response import Response


class admin:

    def GET(self):
        return "<p style='font-family: \"Lucida Console\", Monaco, monospace'>OTTDPoxy: Get is not supported.</p>"

    def POST(self):
        config = Context.get_context().get_config().admin

        if not config.web_host_access is "":
            web.header('Access-Control-Allow-Origin', config.web_host_access)

        response = self.__handlePostRequest(config, web.data())

        if response.error and response.status is 0:
            response.status = 2

        return response.serialize()

    def __handlePostRequest(self, config, requestData):
        response = Response()

        if not config.enabled:
            response.error = 'Admin module is not enabled'
            return response

        request = Request(requestData)

        if not self.__is_authenticated(config, request):
            response.error = 'You are not authenticated to access this resource'
            return response

        if not request.payload or not 'action' in request.payload:
            return response

        type = request.payload['type']

        if type == 'config':
            return self.__game_config(config, request, response)
        elif type == 'game_state':
            return self.__game_config(config, request, response)
        elif type == 'settings':
            return self.__admin_settings(config, request, response)

    def __is_authenticated(self, config, request):
        if config.allow_public:
            return True

        if config.password != '' and config.password == request.password:
            return True

        return False

    def __game_config(self, config, request, response):

        if not os.path.isdir(config.game_config_location):
            response.error = 'path ' + config.game_config_location + " doesn't exist"
            return response

        if 'action' in request.payload:
            action = request.payload['action']
            if action == 'list':
                response.payload['config_files'] = glob.glob(os.path.join(config.game_config_location, config.game_config_filter))

            elif action == 'save':
                if not 'config_file' in request.payload:
                    response.error = 'no config file specified in request'
                    return response
                if not 'config_data' in request.payload:
                    response.error = 'no config data specified in request'
                    return response
                try:
                    f = open(request.payload['config_file'], 'w')
                except IOError as ex:
                    response.error = 'Error opening file: ' + ex.message
                else:
                    with f:
                        try:
                            f.write(base64.b64decode(request.payload['config_data']))
                        except Exception as ex:
                            response.error = 'Error saving file: ' + ex.message

                return response

            elif action == 'get':
                if not 'config_file' in request.payload:
                    response.error = 'no config file specified in request'
                    return response
                try:
                    f = open(request.payload['config_file'], 'r')
                except IOError as ex:
                    response.error =  'Error opening file: ' + ex.message
                else:
                    with f:
                        try:
                            response.payload['config_data'] = base64.b64encode(f.read())
                        except Exception as ex:
                            response.error = 'Error reading file: ' + ex.message

                return response

            elif action == 'delete':
                if not 'config_file' in request.payload:
                    response.error = 'no config file specified in request'
                    return response
                try:
                    os.remove(request.payload['config_file'])
                except IOError as ex:
                    response.error = 'Error removing file: ' + ex.message

                return response

        return response

    def __game_settings(self, config, request, response):
        pass

    def __game_state(self, config, request, response):
        pass