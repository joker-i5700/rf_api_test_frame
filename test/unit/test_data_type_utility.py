# -*- coding: utf-8 -*-
"""
!/usr/bin/python3
@CreateDate   : 2019-07-15
@Author      : jet
@Filename : test_data_type.py
@Software : pycharm
"""
import sys, os
sys.path.append(os.path.abspath("../../"))

import unittest
import HTMLTestRunner
from TestLibrary.infrastructure.Utility.data_type_utility import DataTypeUtility

class DataTypeUtilityTestCase(unittest.TestCase):
    def setUp(self):
        # 每个测试用例执行之前做操作
        self.dtu = DataTypeUtility()
        self.data = {'a': 1, 'list': [{'a': 'abc'},
                             {'c': 1, 'd': 2},
                             [
                                 {'f': 1, 'c': 2},
                                 {'f': 2, 'c': 2},
                                 {'f': 3, 'c': 2},
                                 {'f': 4, 'c': 2}
                                 ]
                             ]
        }
    def tearDown(self):
        # 每个测试用例执行之后做操作
        self.dtu = None
        
    @classmethod
    def tearDownClass(self):
        # 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
        print('---tearDownClass---')
    @classmethod
    def setUpClass(self):
        # 必须使用@classmethod 装饰器,所有test运行前运行一次
        print('---setUpClass---')
       
    def testFind_f_0(self):
        self.assertEqual(self.dtu.get_values_by_keys(self.data, ['list', 2, 0, 'f']), (40, 40))
        
        
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(DataTypeUtilityTestCase("testFind_f_0"))
    # 执行测试
    # runner = unittest.TextTestRunner()
    fp = open('unittest_report.html','wb')#打开一个保存结果的html文件
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='api测试报告',description='测试情况')
    runner.run(suite)
"""
---常用断言---
assertEqual(a, b)     a == b      
assertNotEqual(a, b)     a != b      
assertTrue(x)     bool(x) is True      
assertFalse(x)     bool(x) is False      
assertIsNone(x)     x is None     
assertIsNotNone(x)     x is not None   
assertIn(a, b)     a in b    
assertNotIn(a, b)     a not in b
""" 
        
        
        
        
        
        
        
        
        
        
        
        
        