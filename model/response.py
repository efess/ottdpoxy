from jsonhelper import JsonHelper


class Response:
    def __init__(self):
        self.status = -1
        self.payload = {}
        self.type = ''
        self.action = ''
        self.error = ''

    def serialize(self):
        response = {
            'status': self.status,
            'payload': self.payload,
            'type': self.type,
            'action': self.action
        }
        if not self.status is 0:
            response['error'] = self.error
        return JsonHelper.to_json(response)