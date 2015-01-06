import sys
from servercontroller import ServerController
from config import Config
import getopt


class Poxy:

    @staticmethod
    def main(argv):
        startup = Poxy.parse_arguments(argv)

        if startup['usage']:
            Poxy.print_commandline_help()
            return
        if startup['create_config']:
            Poxy.default_config(startup)
            return

        controller = ServerController(startup)
        controller.start_server()

    @staticmethod
    def parse_arguments(args):
        try:
            parsed_opts, parsed_args = getopt.getopt(args, "dhc:", ["config", 'help', 'config='])
        except getopt.GetoptError as ex:
            print ex.msg
            exit(1)

        startup = {
            'create_config': False,
            'usage': False,
            'config_path': ''
        }
        for opt, arg in parsed_opts:
            if opt in ('-d', '--write-default-config'):
                startup['create_config'] = True
            if opt in ('-h', '--help'):
                startup['usage'] = True
            if opt in ('-c', '--config'):
                startup['config_path'] = arg

        return startup

    @staticmethod
    def print_commandline_help():
        print "Usage: python poxy.py [options]"
        print "\n\t-h,--help \t\tprint this help and exit"
        print "\t-d,--default-config\tWrite the default configuration file and exit"
        print "\t-c,--config\t\tSpecify the path for configuration"

    @staticmethod
    def default_config(startup):
        Config(startup['config_path'], True)

if __name__ == '__main__':
    raise SystemExit(Poxy.main(sys.argv[1:]))
