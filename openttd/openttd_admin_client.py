from libottdadmin2.packets import *
from libottdadmin2.enums import *
from libottdadmin2.adminconnection import AdminConnection
from openttd.receive_thread import ReceiveThread
from openttd.send_thread import SendThread
import logging


class OpenttdAdminClient:

    __the_connection = None

    def __init__(self, openttd_server, message_callback):
        self.__receive_thread = ReceiveThread()
        self.__send_thread = SendThread()
        self.server = openttd_server
        self.message_callback = message_callback

    def connect(self):

        connection = AdminConnection()

        connection.configure(
            name="ottdpoxy",
            password=self.server.password,
            host=self.server.host,
            port=self.server.port
        )

        if not connection.connect():
            logging.warning("Could not connect to " + self.server.name)
            return None

        self.__receive_thread.start()
        self.__send_thread.start()


    def send_message(self):
        self.__send_thread.send_packet()
        pass
#
# main thread - start app. Listen for web requests?
# server_man thread - Respoond to game events (Game Event Thread)
#     read_thread - listen to game socket
#     send_thread - write to game socket
#
#
# eew
#
# read thread
# write thread
#
# client - producer
#
#
# controller - consumer
#
#     config manager - responsible for copying new config when game changes

