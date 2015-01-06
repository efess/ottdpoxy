from jsonhelper import JsonHelper


class Request:
    def __init__(self, data):
        self.password = ''
        req_data = JsonHelper.from_json(data)
        if not 'payload' in req_data:
            return
        if 'password' in req_data:
            self.password = req_data['password']

        self.payload = req_data['payload']