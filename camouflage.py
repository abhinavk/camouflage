# Camouflage module
import argparse
import os
import json


class Camouflage():
    '''Camouflage class'''
    def __init__(self, opt, target, config):
        '''Constructor for Camouflage class. Opens and parses the file'''
        self.option = opt
        self.target = target
        with open(config, 'r') as cfg:
            try:
                self.ccfg = json.load(cfg)
            except ValueError:
                print('Config Decoding failed ')
                return

    def execute(self):
        '''Run the hider/unhider'''
        try:
            with open(self.target, 'r') as file:
                file_content = file.read()
        except IOError:
            print('Cannot read file')
            return

        if self.option:
            file_content = self.hide(file_content)
        else:
            file_content = self.unhide(file_content)

        try:
            with open(self.target, 'w') as file:
                file.write(file_content)
        except IOError:
            print('Cannot write file')
            return

    def hide(self, text):
        for i in self.ccfg.keys():
            text = text.replace(i, '{{ ' + self.ccfg[i] + ' }}')
        return text

    def unhide(self, text):
        for i in self.ccfg.keys():
            text = text.replace('{{ ' + self.ccfg[i] + ' }}', i)
        return text


def main():
    '''Run the program with specified arguments'''

    argparser = argparse.ArgumentParser(description='Camouflage')
    argparser.set_defaults(opt=True,config='camouflage.json')
    argparser.add_argument('target', action='store', help='Specify the target file')
    group = argparser.add_mutually_exclusive_group(required=False)
    group.add_argument('-s', '--hide', action='store_true', dest='opt', help='Hide stuff')
    group.add_argument('-u', '--unhide', action='store_false', dest='opt', help='Unhide stuff')
    argparser.add_argument('-c', '--config', action='store', dest='config', help='Specify the config file (Default is ./camouflage.json)')
    args = argparser.parse_args()

    camouflage = Camouflage(args.opt, args.target, args.config)
    camouflage.execute()


if __name__ == '__main__':
    main()
