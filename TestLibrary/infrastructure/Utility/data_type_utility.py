# -*- coding: utf-8 -*-
"""
!/usr/bin/python3
@CreateDate   : 2019-07-17
@Author      : jet
@Filename : data_type_urility.py
@Software : pycharm
"""

import copy
from .Logger import logger

class DataTypeUtility(object):
    
    def __init__(self):
        pass

    def get_values_by_keys(self, data, keys):
        """
                        输入指定格式的KEY列表，返回一个列表，包含DATA字典中所有符合要求的VALUE
        :param data: 字典类型变量，支持字典、列表多层混合嵌套
        :param keys: 列表类型变量参数
                                                                参数1：指定DATA字典中的一个KEY
                                                                参数2~(n-1)：指定在KEY的VALUE中，具体那个节点进行查找
                                                                                                值为*则表示在所有结点中查找
                                                                参数n：指定要查找结点中的KEY值
        :return: 列表类型，返回所有指定KEY对应的VALUE值
        """
        logger.info("DataTypeUtility.get_values_by_keys  ->  data: {0},keys: {1}".format(data, keys))
        values = []
        DataTypeUtility._get_values_by_keys(data, values, keys)
        #logger.info("values: {0}, \nkeys: {1}".format(values, keys))
        return values

    @staticmethod
    def _get_values_by_keys(data, values, keys):
        #logger.info("data: {0}, values: {1}, keys: {2}".format(data, values, keys))
        if isinstance(data, dict):
            DataTypeUtility._get_values_from_dict(data, values, keys)
        elif isinstance(data, list):
            DataTypeUtility._get_values_from_list(data, values, keys)
        else:
            values.append(data)

    @staticmethod
    def _get_values_from_list(data, values, keys):
        #logger.info("list data: {0}, values: {1}, keys: {2}".format(data, values, keys))
        tmpData = copy.deepcopy(data)
        if '*' == keys[0]:
            for subData in tmpData:
                DataTypeUtility._get_values_by_keys(subData, values, keys[1:])
        else:
            DataTypeUtility._get_values_by_keys(
                tmpData[keys[0]], values, keys[1:])

    @staticmethod
    def _get_values_from_dict(data, values, keys):
        #logger.info("dict data: {0}, values: {1}, keys: {2}".format(data, values, keys))
        tmpData = copy.deepcopy(data)
        if '*' == keys[0]:
            for subkey in tmpData:
                DataTypeUtility._get_values_by_keys(
                    tmpData[subkey], values, keys[1:])
        else:
            DataTypeUtility._get_values_by_keys(
                tmpData[keys[0]], values, keys[1:])
            
    def get_values_by_key(self, data, key):
        """
                        输入一个KEY值，返回一个列表，包含DATA字典中所有此KEY的VALUE
        :param data: 字典类型变量，支持字典、列表多层混合嵌套
        :param key: 字符串类型，指定一个KEY
        :return: 列表类型，返回包含DATA字典中所有此KEY的VALUE
        """
        logger.info("DataTypeUtility.get_values_by_key  ->  data: {0},key: {1}".format(data, key))
        self.lisValue = []
        self._get_values_by_key(data, key)
        return self.lisValue

    def _get_values_by_key(self, data, name):
        # logger.debug("input data : %s" % data)
        # logger.debug("input name : %s" % name)
        if type(data).__name__ == 'dict':
            # logger.debug("parse dict...")
            if name in data.keys():
                # logger.debug("append value : %s" % data[name])
                self.lisValue.append(data[name])
            else:
                for key in data.keys():
                    # print 'ssss %s' % data
                    newData = data[key]
                    if type(newData).__name__ == 'dict':
                        # logger.debug("parse dict......")
                        # data = newData[key]
                        # print ('data1 %s' % data)
                        self._get_values_by_key(newData, name)
                    if type(newData).__name__ == 'list':
                        # logger.debug("parse list......")
                        for i in range(len(newData)):
                            tempData = newData[i]
                            self._get_values_by_key(tempData, name)

        if type(data).__name__ == 'list':
            # logger.debug("parse list...")
            for i in range(len(data)):
                tempData = data[i]
                # print ('tempData %s' % tempData)
                self._get_values_by_key(tempData, name)



if __name__ == '__main__':
    data = {'a': 1, 'list': [{'a': 'abc'},
                             {'c': 1, 'd': 2},
                             [
                                 {'f': 1, 'c': 2},
                                 {'f': 2, 'c': 2},
                                 {'f': 3, 'c': 2},
                                 {'f': 4, 'c': 2}
    ]
    ]}
    print(DataTypeUtility.get_values_by_keys(data, ['list', 2, 0, 'c']))
