# -*- coding: utf-8 -*-
"""
!/usr/bin/python3
@CreateDate   : 2019-07-09
@Author      : jet
@Filename : RequestParse.py
@Software : eclipse + RED
"""
import re, random, string
import urllib
from urllib.parse import quote
import hashlib
import hmac
import time
from datetime import date
import binascii
from TestLibrary.infrastructure.Parse.JsonParse import JsonParse
from TestLibrary.infrastructure.Utility.Logger import logger
from TestLibrary.infrastructure.Utility.AESCipher import AESCipher


class RequestParse(object):
    lisValue = []

    def __init__(self):
        pass

    def kw_body_parse(self, content, key):
        '''
                        说明：将字符串转换为json格式并取出指定的key

                         参数:
                |  content (string)                      | 输入一个字符串，通常为返回消息体的content字段                                  |
                |  key (string)                      | 指定一个Key值                                  |

                        返回值：
                |  return value (String)                      | 返回取出指定的key        |
                        例子:

        | *Keywords*           |  *Parameters*                                      |
        | Kw Body Parse           |  ${response.content}  | requestType   |
        '''
        content_json = JsonParse.content_to_json(content)
        return JsonParse.get_from_json(content_json, key)

    def kw_body_tojson(self, content):
        '''
                        说明：将字符串转化为json对象

                        参数:
                |  content (string)                      | 输入一个字符串，通常为返回消息体的content字段                                  |

                        返回值：
                |  return value (String)                      | 返回json类型对象        |
                        例子:

        | *Keywords*           |  *Parameters*                                      |
        | kw body tojson           |  ${response.content}  |
        '''
        return JsonParse.content_to_json(content)

    def kw_dict_update_parse(self, originDict, changeDict):
        '''
                       说明：更新字典的值，如果key值不存在，则新增字典项

                        参数:
                |  originDict (dict)                      | 初始字典值                                 |
                |  changeDict (dict)                      | 需要更新的字典值（k:v）                                 |

                        返回值：
                |  return value (String)                      | 将更新好的字典以字符串形式返回        |
                        例子:

        |            | *Keywords*           |  *Parameters*                                      |
        | ${strdic}    | Set Variable    | {1: 'a', 2: 3, 3: 'test', 4: 100}                   |
        | ${rstrdic}    | Set Variable    | {1:'b',2: 5}                                       |
        | ${ret}    | kw dict update parse    | ${strDic}    | ${rstrdic}                       |
        | log    | ${ret}                                                                     |
        '''
        if originDict and not isinstance(originDict, dict):
            originDict = eval(originDict)
        if changeDict and not isinstance(changeDict, dict):
            changeDict = eval(changeDict)
        logger.info(
            "Input >>> originDict : {0} , changeDict : {1}".format(
                originDict, changeDict))
        originDict.update(changeDict)
        logger.info("Output <<< originDict : {0}".format(originDict))

        nr = str(originDict).replace("\'", "\"")
        return nr
    

    def kw_expire_date(self, data):
        exp_date = ""
        ldata = data.split('&')
        for kv in ldata:
            lkv = kv.split('=')
            if "expire" == lkv[0]:
                exp_date = lkv[1]

        if "----" == exp_date:
            return exp_date

        cur_date = time.strftime('%Y%m%d', time.localtime())
        s_exp_date = date(int(exp_date[:4]), int(
            exp_date[4:6]), int(exp_date[-2:]))
        s_cur_date = date(int(cur_date[:4]), int(
            cur_date[4:6]), int(cur_date[-2:]))

        r_timedelta = s_exp_date - s_cur_date

        return r_timedelta.days
