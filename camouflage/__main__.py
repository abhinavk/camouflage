"""
__main__.py for directly calling the program in shell
"""

import argparse
import camouflage


def create_console_arguments():
    '''
    Create arguments for the console program.
    target = File to be modified
    Configuration files
    Hide or Unhide operation
    '''

    argparser = argparse.ArgumentParser(description='Camouflage - A tool to \
        replace sensitive data from your source files')
    argparser.set_defaults(opt=True, config='camouflage.json')

    # Target is a required Positional Argument
    argparser.add_argument(
        'target', action='store', help='Specify the target file')
    # --config is optional. Camouflage.json will be used as default
    config_group = argparser.add_mutually_exclusive_group(required=False)
    config_group.add_argument(
        '-c', '--config', action='store', dest='config',
        help='Specify the config file (Default is ./camouflage.json)')
    config_group.add_argument(
        '-g', '--global', action='store_true', dest='config',
        help='Use the global configuration file in Home folder')

    # --hide and --unhide arguments must not be specified together
    action_group = argparser.add_mutually_exclusive_group(required=False)
    action_group.add_argument(
        '-s', '--hide', action='store_true', dest='opt', help='Hide stuff')
    action_group.add_argument(
        '-u', '--unhide', action='store_false', dest='opt', help='Unhide stuff'
    )

    return argparser.parse_args()


def main():
    '''
    Instantiate Camouflage class and call execute()
    '''

    args = create_console_arguments()

    # Pass option, target file name, config file name to the constructor
    cflage = camouflage.Camouflage(args.opt, args.target, args.config)
    cflage.execute()


if __name__ == '__main__':
    main()
