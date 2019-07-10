# -*- coding: utf-8 -*-
"""
!/usr/bin/python3
@CreateDate   : 2019-07-09
@Author      : jet
@Filename : ConfigOperator.py
@Software : eclipse + RED
"""

import configparser

class ConfigOperator(object):

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    config = None

    def __init__(self, filepath):
        self.config = None
        self.configfile = filepath

    def get_sections(self):
        if(self.config == None):
            self.config = configparser.ConfigParser()
            self.config.read(self.configfile)
        return self.config.sections()

    def get_items(self, section_name):
        if(self.config == None):
            self.config = configparser.ConfigParser()
            self.config.read(self.configfile)
        return self.config.items

    def add_item(self, section_name, key_name, key_value):
        if(self.config == None):
            self.config = configparser.ConfigParser()
            self.config.read(self.configfile)
        try:
            self.config.add_section(section_name)
        except:
            pass
        self.config.set(section_name, key_name, key_value)
        self.config.write(open(self.configfile, 'w'))

    def get_value(self, section_name, key_name):
        if(self.config == None):
            self.config = configparser.ConfigParser()
            self.config.read(self.configfile)
        return self.config[section_name][key_name]

    def set_value(self, section_name, key_name, key_value):
        if(self.config == None):
            self.config = configparser.ConfigParser()
            self.config.read(self.configfile)
        self.config.set(section_name, key_name, key_value)
        self.config.write(open(self.configfile, 'w'))

    def remove_item(self, section_name, key_name):
        if(self.config == None):
            self.config = configparser.ConfigParser()
            self.config.read(self.configfile)
        self.config.remove_option(section_name, key_name)
