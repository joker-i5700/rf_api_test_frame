# -*- coding: utf-8 -*-
"""
!/usr/bin/python3
@CreateDate   : 2019-07-09
@Author      : jet
@Filename : MysqlService.py
@Software : eclipse + RED
"""
import errno

from TestLibrary.infrastructure.Persistence.MysqlOperator import MysqlOperator

class MysqlService(object):

    def __init__(self):
        self.mysql_operator = None
        self.mysql_connected = False

    def kw_mysql_connect(self, dbhost, dbname, username, password):
        '''连接数据库，连接正常返回true，否则返回false'''
        self.mysql_operator = MysqlOperator(dbhost, dbname, username, password)
        self.mysql_connected = self.mysql_operator.connect()
        if(self.mysql_connected == True):
            return True
        else:
            return False

    def kw_mysql_query(self, sql):
        '''数据库查询，返回查询列表'''
        if(self.mysql_connected == True):
            return self.mysql_operator.query(sql)
        else:
            raise errno.Error("connect db failed")

    def kw_mysql_update(self, sql):
        '''数据库增、删、改，执行成功返回true，否则返回false'''
        if (self.mysql_connected == True):
            return self.mysql_operator.execute(sql)
        else:
            raise errno.Error("connect db failed")

    def kw_mysql_release(self):
        '''关闭数据库'''
        self.mysql_operator.release()

if __name__ == "__main__":
    pass

