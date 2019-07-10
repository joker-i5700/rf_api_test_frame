# -*- coding: utf-8 -*-
'''
!/usr/bin/python3
@CreateDate   : 2019-07-09
@Author      : jet
@Filename : MysqlOperator.py
@Software : eclipse + RED
'''
import pymysql

class MysqlOperator(object):

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, db_host, db_name, db_username, db_password):
        self.host = db_host
        self.dbname = db_name
        self.username = db_username
        self.password = db_password

        self.db_obj = None
        self.cursor = None
        self.connect_status = 0

    #connect db
    def connect(self):
        try:
            self.db_obj = pymysql.connect(self.host, self.username, self.password, self.dbname)
            self.cursor = self.db_obj.cursor()
            self.connect_status = 1
        except Exception as ex:
            self.connect_status = 0
            print(ex)
        return self.connect_status

    #excute sql
    def execute(self, sql):
        if(self.connect_status == 1 ):
            try:
                self.cursor.execute(sql)
                self.db_obj.commit()
                return 1
            except Exception as ex:
                self.db_obj.rollback()# rollback when error
                return 0
        else:
            print("Database Error,not connect")


    def query(self, sql):
        if (self.connect_status == 1):
            try:
                self.cursor.execute(sql)
                results = self.cursor.fetchall()
                return results
            except Exception as ex:
                print(ex)
                return None
        else:
            print("Database Error,not connect")

    def release(self):
        try:
            self.db_obj.close()
        except:
            pass

if __name__ == "__main__":
    pass
    # mysql = MysqlOperator("127.0.0.1", "db_name", "db_user", "db_pwd")
    # mysql.connect()