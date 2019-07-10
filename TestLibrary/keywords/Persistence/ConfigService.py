# -*- coding: utf-8 -*-
"""
!/usr/bin/python3
@CreateDate   : 2019-07-09
@Author      : jet
@Filename : ConfigService.py
@Software : eclipse + RED
"""
from TestLibrary.infrastructure.Persistence.ConfigOperator import  ConfigOperator

class ConfigService(object):
    configOperator = None

    def __init__(self):
        self.configOperator = None

    def kw_config_get_value(self, section_name, key_name):
        '''获取指定配置的值'''
        if(self.configOperator == None):
            self.configOperator = ConfigOperator('config')
        return self.configOperator.get_value(section_name, key_name)

    def kw_config_set_value(self, section_name, key_name, key_value):
        '''设置指定配置的值'''
        if(self.configOperator == None):
            self.configOperator = ConfigOperator('config')
        return self.configOperator.set_value(section_name, key_name, key_value)

    def kw_config_add_item(self, section_name, key_name, key_value):
        '''增加配置项'''
        if(self.configOperator == None):
            self.configOperator = ConfigOperator('config')
        return self.configOperator.add_item(section_name, key_name, key_value)

    def kw_config_remove_item(self, section_name, key_name):
        '''删除指定配置的值'''
        if(self.configOperator == None):
            self.configOperator = ConfigOperator('config')
        return self.configOperator.remove_item(section_name, key_name)

if __name__ == "__main__":
    cs = ConfigService()
    print(cs.kw_config_get_value("public", "version"))