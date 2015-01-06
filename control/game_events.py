import threading
import Queue
from pub_sub import PubSub


class GameEvents (threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.__messages = Queue.Queue()

    def run(self):
        self.__consumer_thread()

    def add_message(self, message):
        self.__messages.put(message)

    def __consumer_thread(self):
        while True:
            message = self.__messages.get(True)
            if message.name is 'NewGame':
                PubSub.publish("openttd/new_game")

