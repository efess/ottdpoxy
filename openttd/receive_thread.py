import threading
import Queue

class ReceiveThread(threading.Thread):

    def __init__(self, admin_connection):
        threading.Thread.__init__(self)
        self._received_packets = Queue.Queue()
        self._admin_connection = admin_connection

    def run(self):
        self._receive_loop()

    def _receive_loop(self):
        while self._admin_connection.is_connected():
            self._received_packets.put(self._admin_connection.recv_packet())