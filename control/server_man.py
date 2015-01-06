from game_events import GameEvents
from pub_sub import PubSub
from openttd.openttd_admin_client import OpenttdAdminClient


class ServerMan:

    def __init__(self, openttd_server):
        self.game_events = GameEvents()
        self.admin_client = OpenttdAdminClient(openttd_server)

    def _hookup_events(self):
        PubSub.subscribe("openttd/new_game", self._on_newgame)

    def _on_newgame(self):
        pass

