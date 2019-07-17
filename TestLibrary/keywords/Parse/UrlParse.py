# -*- coding: utf-8 -*-
"""
!/usr/bin/python3
@CreateDate   : 2019-07-15
@Author      : jet
@Filename : UrlParse.py
@Software : pycharm
"""

from TestLibrary.infrastructure.Utility.Logger import logger
from TestLibrary.infrastructure.Utility.url_utility import UrlUtility


class UrlParse:
    def __init__(self):
        pass
        
    def kw_generate_url(self, *args, **kargs):
        uu = UrlUtility()
        return uu.generate_url(*args, **kargs)
    
    def kw_parse_url(self,  *urls):
        uu = UrlUtility()
        return uu.parse_url(*urls)
    
    def kw_get_path_by_replace_host_port(self, url, hostAndport):
        uu = UrlUtility()
        return uu.get_path_by_replace_host_port(url, hostAndport)
    
    def kw_get_path_by_replace_query_params(self, url, queryParams):
        uu = UrlUtility()
        return uu.get_path_by_replace_query_params(url, queryParams)
    
    def kw_get_host_port_with_prefix(self, url):
        uu = UrlUtility()
        return uu.get_host_port_with_prefix(url)

    
    