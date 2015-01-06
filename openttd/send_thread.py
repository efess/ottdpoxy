import threading
import Queue


class SendThread(threading.Thread):

    def __init__(self, admin_connection):
        threading.Thread.__init__(self)
        self._send_packets = Queue.Queue()
        self._admin_connection = admin_connection

    def run(self):
        self._send_loop()

    def send_packet(self, packet):
        self._send_packets.put(packet)

    def _send_loop(self):
        while self._admin_connection.is_connected():
            packet = self._send_packets.get()  # will block
            self._admin_connection.send_packet(packet)
