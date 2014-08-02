"""Camouflage module"""

import json
import mimetypes
import os


class Camouflage():

    '''Camouflage class'''

    def __init__(self, target, config, hide_action=True, backup=False):
        '''
        Constructor for Camouflage class
        hide_action - if True runs in hide mode else in unhide mode
        target - target file
        config - configuration file
        cformat - configuration file format (JSON, YAML or XML)
        '''
        self.hide_action = hide_action
        self.target = target
        self.config = config
        self.backup_original = backup

    def execute(self):
        '''Run the hider/unhider'''
        # Parse the configuration file according to its content type
        try:
            parser = ConfigurationParser(self.config)
        except IOError:
            print('Cannot process configuration file')
            return
        else:
            self.ccfg = parser.parse_config()

        self.read_file()

        # Call hide/unhide functions as per the value passed in hide_action
        # to replace text
        if self.hide_action:
            new_file_content = self.__hide(self.file_content)
        else:
            new_file_content = self.__unhide(self.file_content)

        if new_file_content == self.file_content:
            print('Nothing changed')
        else:
            if self.backup_original:
                self.__backup_original_file()
            self.write_file(new_file_content)

    def write_file(self, file_content):
        '''Write the modified file to the disk'''
        try:
            with open(self.target, 'w') as file:
                file.write(file_content)
        except IOError:
            print('Cannot write file')
            return

    def read_file(self):
        '''Read target file'''
        try:
            with open(self.target, 'r') as file:
                self.file_content = file.read()
        except IOError:
            print('Cannot read file')
            return

    def __hide(self, text):
        for i in self.ccfg.keys():
            # Use Liquid-style placeholders
            text = text.replace(i, '{{ ' + self.ccfg[i] + ' }}')
        return text

    def __unhide(self, text):
        for i in self.ccfg.keys():
            text = text.replace('{{ ' + self.ccfg[i] + ' }}', i)
        return text

    def __backup_original_file(self):
        '''
        Create a backup of the original file
        '''
        backup_url = os.path.join(os.path.dirname(self.target), self.target + '.bak')
        with open(backup_url) as file:
            file.write(self.file_content)


class ConfigurationParser:

    '''Parse the configuration file as per its content type'''

    def __init__(self, config_file):
        '''
        Constrcutor for ConfigurationParser class
        config_file - Path to configuration file
        '''
        self.cfg = config_file
        self.cfg_type, self.cfg_encoding = mimetypes.guess_type(self.cfg)

        if self.cfg_type is None:
            raise IOError

    def parse_config(self):
        '''
        Parse the configuration file
        '''
        if self.cfg_type == 'application/json':
            with open(self.cfg) as file:
                return self.__parse_json(file)

    def __parse_json(self, file):
        try:
            json_dict = json.load(file)
        except ValueError:
            print('Config Decoding failed ')
            return None
        return json_dict
