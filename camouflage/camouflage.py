"""Camouflage module"""

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
            file_content = self.__hide(file_content)
        else:
            file_content = self.__unhide(file_content)

        try:
            with open(self.target, 'w') as file:
                file.write(file_content)
        except IOError:
            print('Cannot write file')
            return

    def __hide(self, text):
        for i in self.ccfg.keys():
            text = text.replace(i, '{{ ' + self.ccfg[i] + ' }}')
        return text

    def __unhide(self, text):
        for i in self.ccfg.keys():
            text = text.replace('{{ ' + self.ccfg[i] + ' }}', i)
        return text
