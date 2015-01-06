from configsection import *
from jsonhelper import JsonHelper
from os import path


class Config:
    __default_filename = "config.json"
    __full_path = ''

    def __init__(self, config_path='', dump_default=False):
        if config_path:
            Config.__full_path = config_path
        else:
            Config.__full_path = path.join(Config.__default_filename)

        if dump_default or not self.load():
            self.config = Config.__default()
            self.save()

    @property
    def instance(self):
        return GameInstance(**self.config['ottdpoxy']['config']['game_instance'])

    @property
    def general(self):
        return GeneralConfig(**self.config['ottdpoxy']['config']['general'])

    @property
    def admin(self):
        return AdminConfig(**self.config['ottdpoxy']['config']['admin'])

    @property
    def stats(self):
        return StatsConfig(**self.config['ottdpoxy']['config']['stats'])

    def load(self):
        try:
            self.config = JsonHelper.from_json_file(Config.__full_path)
            return True
        except IOError:
            return False

    def save(self):
        try:
            JsonHelper.to_json_file(self.config, Config.__full_path)
        except IOError:
            pass

    @staticmethod
    def __default():
        return {
                    "ottdpoxy":
                    {
                        "config":
                        {
                            "game_instance":
                            {
                                "name": "server1",
                                "host": "localhost",
                                "port": 3977,
                                "password": ""
                            }
                            ,
                            "admin": {
                                "enabled": True,
                                "password": "",
                                "web_host_access": "*",
                                "game_config_location": '/home/openttd/.openttd',
                                "game_config_filter": '*.cfg',
                                "ofs_script_location": '/home/openttd/ofs'
                            }
                            ,
                            "stats": {
                                "enabled": True,
                                "password": "",
                                "allow_public": True,
                                "internal_poll_interval": 30,
                                "web_host_access": "*"
                            }
                            ,
                            "general": {
                                "listen_port": 3077
                            }
                        }

                    }
                }