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

    def kw_body_parse_ex(self,data,key):
        '''
                        说明：将字符串转换为json格式并取出指定key所对应的所有Value
                        
                        参数：
                |  data (dict or list)                      | 字典、列表混合类型                                |
                |  key (String)                      | 要查找的key值                                 |
                
                        返回值：
                |  return value (list)                      | 返回一个列表，包含key值对应的所有value        |
                        例子：
            |            | *Keywords*           |  *Parameters*                                      |  
            | ${data}    | Set Variable    | {"code": "ss", "rows":[{"id": 1, "value": "test"},{"id": 2, "value": "ress"}]}    |
            | ${retData1}    | xl ret jsonKey parse    | ${data}    | id  |                  
        '''
        self.lisValue = []
        jsonData = JsonParse.content_to_json(data)
        self._get_from_json_ex(jsonData,key)   
        return    self.lisValue 
    
    def _get_from_json_ex(self,data, name):
        logger.debug("input data : %s" % data)
        logger.debug("input name : %s" % name)
        if type(data).__name__ == 'dict':
            logger.debug("parse dict...")
            if name in data.keys():
                logger.debug("append value : %s"  % data[name])
                self.lisValue.append(data[name])
            else:
                for key in data.keys():
                    #print 'ssss %s' % data
                    newData = data[key]
                    if type(newData).__name__ == 'dict':
                        logger.debug("parse dict......")
                        #data = newData[key]
                        #print ('data1 %s' % data)
                        self._get_from_json_ex(newData, name)
                    if type(newData).__name__ == 'list':
                        logger.debug("parse list......")
                        for i in range(len(newData)):
                            tempData = newData[i]
                            self._get_from_json_ex(tempData, name)
    
        if type(data).__name__ == 'list':
            logger.debug("parse list...")
            for i in range(len(data)):
                tempData = data[i]
                #print ('tempData %s' % tempData)
                self._get_from_json_ex(tempData, name)

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
    
    def kw_boundary_generate(self, dict, bran):
        """ 说明：输入字典${dict}（key:value对）与${bran},生成from-data协议的数据格式string
                                   
                                   参数：
                |  dict (dict)                      | 输入一个字典                                |
                |  bran (String)                      |  from-data 格式分隔符                               |
                
                                    
                                    返回值：
                |  return value (String)                      | from-data协议的数据格式string body        |   
                
                                    例子：
                |            | *Keywords*           |  *Parameters*                                      |
                | ${dc}    | Evaluate    | {"sessionType":0,"clientSecret":100,"appid":100,"appName":"WEB-i.xxx.com"}    |
                | ${st}=    | Set Variable    | ------WebKitFormBoundary5rFTEqcX0liWDgE8    |
                | ${ret}    | xl boundary generate    | ${dc}    | ${st}   |
                | Log    | ${ret}    |
        """
        rs = ""
        lis = []
        for k,v in dict.items():
            lis.append(bran)
            lis.append('Content-Disposition: form-data; name=\"' + k + '\"')
            lis.append("")
            lis.append(str(v))
    
        for s in lis:
            rs = rs + s + "\r\n"
    
        rs = rs + bran + "--"
        return rs
    
    def kw_cover_get_Parameters(self,gStr,dict):
        """
                                说明：输入get请求参数串和要替换的key-value，更新get请求参数串
                               
                               参数：
                |  gStr (String)                      | Get请求字符串                              |
                |  dict (dict)                      | 需要修改的值（k:v）                               |
                                    
                                返回值：
                |  return value (String)                      | 已更新的Get请求字符串       |
                
                               例子：
                |            | *Keywords*           |  *Parameters*                                      |   
                | ${s}    | Set Variable    | appid=11&Version=10&appName=com.xxx.sdk&clientVersion=v1.0.0&deviceid=abcdefg1234567  |
                | ${d}    | Evaluate    | {'appid': '123', 'appName': 'com.jet.sdk', 'deviceid': 'hijkl89012'}   |
                | ${retStr}    | kw cover get Parameters    | ${s}    ${d}   |
                | Log    | ${retStr}       |           
                                
        """
        if "&" != gStr[-1:]:
            gStr = gStr + "&"
        for k,v in dict.items():
            gStr = re.sub(str(k) + '=(.+?)&', str(k) + "=" + str(v) + "&", gStr)
        return gStr[:-1]
    


