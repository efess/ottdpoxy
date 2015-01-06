from jsonhelper import JsonHelper


class AdminSettings:
    __default_filename = "admin_config.json"

    @staticmethod
    def load():
        try:
            return JsonHelper.from_json_file(AdminSettings.__default_filename)
        except IOError:
            return None

    @staticmethod
    def save(config):
        try:
            JsonHelper.to_json_file(config, AdminSettings.__default_filename)
        except IOError:
            pass

    @staticmethod
    def __default():
        return {
                    "ottdpoxy":
                    {
                        "admin_settings":
                        {
                        }

                    }
                }