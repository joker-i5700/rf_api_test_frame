# -*- coding: utf-8 -*-
"""
!/usr/bin/python3
@CreateDate   : 2019-07-15
@Author      : jet
@Filename : UrlParse.py
@Software : pycharm
"""

from TestLibrary.infrastructure.Utility.Logger import logger
from TestLibrary.infrastructure.Utility.url_urility import UrlUrility


class UrlParse:
    def __init__(self):
        pass
        
    def kw_generate_url(self, *args, **kargs):
        # logger.info(args)
        uu = UrlUrility()
        return uu.generate_url(*args, **kargs)
    
    def kw_test(self):
        print("test")
    
    