class Event:
    def __init__(self, event_name):
        self.__event_name = event_name
        self.__event_handlers = []

    def publish(self, event_info):
        for handler in self.__event_handlers:
            handler(event_info)

    def get_name(self):
        return self.__event_name