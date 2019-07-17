# -*- coding: utf-8 -*-
"""
!/usr/bin/python3
@CreateDate   : 2019-07-17
@Author      : jet
@Filename : DataTypeUtility.py
@Software : pycharm
"""

from TestLibrary.infrastructure.Utility.Logger import logger
from TestLibrary.infrastructure.Utility.data_type_utility import DataTypeUtility


class KwDataTypeUtility:
    def __init__(self):
        pass
        
    def kw_get_values_by_keys(self, data, keys):
        dtu = DataTypeUtility()
        return dtu.get_values_by_keys(data, keys)
    
    def kw_get_values_by_key(self, data, key):
        dtu = DataTypeUtility()
        return dtu.get_values_by_key(data, key)
    

    
    