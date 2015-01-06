class Context:

    __current_context = None

    def __init__(self):
        if Context.__current_context is None:
            self.__config = None
            self.__openttd = None
            Context.__current_context = self

    @staticmethod
    def get_context():
        return Context.__current_context

    def get_config(self):
        return self.__config

    def set_config(self, config):
        self.__config = config

    def get_openttd(self):
        return self.__openttd

    def set_openttd(self, openttd):
        self.__openttd = openttd



        # server tools
        #     new game
        #         map save
        #         config something