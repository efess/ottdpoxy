class ConfigSection:
    def __init__(self, **config_entries):
        self.__dict__.update(config_entries)


class GeneralConfig(ConfigSection):
    def __init__(self, **config):
        ConfigSection.__init__(self, **config)


class GameInstance(ConfigSection):
    def __init__(self, **config):
        ConfigSection.__init__(self, **config)


class StatsConfig(ConfigSection):
    def __init__(self, **config):
        ConfigSection.__init__(self, **config)


class AdminConfig(ConfigSection):
    def __init__(self, **config):
        ConfigSection.__init__(self, **config)