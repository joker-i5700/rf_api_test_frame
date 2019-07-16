# -*- coding: utf-8 -*-
"""
!/usr/bin/python3
@CreateDate   : 2019-07-15
@Author      : jet
@Filename : url_urility.py
@Software : pycharm
"""
import re
from .Logger import logger
from urllib import parse as ps


EMPTY = [None, "", {}, []]

class UrlUrility:
    def __init__(self):
        pass
    

    def generate_url(self, *args, **kargs):
        """
        *args：输入数据长度不确定，通过*args将任意长度的参数传递给函数，系统自动将任意长度参数用list表示
        **kargs：输入数据长度不确定，系统自动将任意长度参数用dict（字典）表示
                        输入两个变长参数，生成URL
        :param args: 长度不确定的可变参数，输入类型为列表，列表中的每个字段为URL PATH的一部分
        :param kargs: 长度不确定的可变参数，输入类型为字典，字典中的每个K-V为URL PARAM的一部分
        :return: 生成一段URL
        """
        logger.info("UrlUrility.generate_url args:%s,kargs:%s" % (args, kargs))
        sep = u'/'
        tempUrl = sep.join([temp.strip(sep)
                            for temp in args if temp not in EMPTY]) if args else ''
        if args and args[0].startswith(sep):
            tempUrl = u'/{0}'.format(tempUrl)  # 'u'/'+ tempUrl
        if kargs:
            tempUrl += u'?'
            tempUrl += u'&'.join([key + '=' + str(value)
                                  for key, value in kargs.items()])
        return tempUrl
    
    
    def parse_url(self, *urls):
        """
                        输入一组URL列表，返回一个列表类型变量，包含多个字典，每个字典对应一个URL列表中的一个URL的解析
                        用户可以根据列表的顺序和指定的KEY值方便的取出任意一个URL中的任意一个字段的值
        :param urls: URL列表集合
        :return: 返回一个列表类型变量，包含多个字典
        """
        resultList = []
        for url in urls:
            urlDict = {}
            parsedUrl = ps.urlparse(url)
            urlDict['hostname'] = parsedUrl.hostname
            urlDict['netloc'] = parsedUrl.netloc
            urlDict['path'] = parsedUrl.path
            urlDict['port'] = parsedUrl.port
            urlDict['queryParams'] = {}
            if parsedUrl.query:
                queryParams = [key.split('=', 1)
                               for key in parsedUrl.query.split('&')]
                print('parsedUrl.query', parsedUrl.query)
                print('queryParams', queryParams)
                urlDict['queryParams'] = {queryParam[0]: queryParam[1]
                                          for queryParam in queryParams if len(queryParam) == 2}
            urlDict['scheme'] = parsedUrl.scheme
            resultList.append(urlDict)
        return resultList
    
    
    def get_path_by_replace_host_port(self, url, hostAndport):
        """
                        替换URL中的IP:PORT
        :param url: 一个URL字符串变量
        :param hostAndport: 字符串变量，要替换的IP:PORT
        :return: 字符串变量，返回一个URL，其中的IP:PORT已被刷新
        """
        parseResult = ps.urlparse(url)
        scheme = parseResult.scheme + '://' if parseResult.scheme else ''
        path_and_params = parseResult.path + \
        ('?' + parseResult.query) if parseResult.query else parseResult.path
        return '{0}{1}{2}'.format(scheme, hostAndport, path_and_params)
    
    def get_path_by_replace_query_params(self, url, queryParams):
        """
                        将URL中的QUERY参数信息，更新为输入字典参数对应的VALUE值
        :param url: 字符串类型URL
        :param queryParams: 字典类型，输入要替换指定KEY的VALUE
        :return: 字符串类型，更新后的URL
        """
        parseResult = ps.urlparse(url)
        scheme = parseResult.scheme + '://' if parseResult.scheme else ''
        query_params = parseResult.query
        if "&" != query_params[-1:]:
            query_params = query_params + "&"
        for k, v in queryParams.items():
            query_params = re.sub(
                str(k) + '=(.+?)&',
                str(k) + "=" + str(v) + "&",
                query_params)
        return '{0}{1}{2}?{3}'.format(
            scheme, parseResult.netloc, parseResult.path, query_params[:-1])
    
    
    def get_host_port_with_prefix(self, url):
        """
                        输入一个URL返回协议头+IP:PORT
        :param url: 一个URL字符串变量
        :return: 协议头+IP:PORT
        """
        parseResult = ps.urlparse(url)
        scheme = parseResult.scheme + '://' if parseResult.scheme else ''
        return '{0}{1}'.format(scheme, parseResult.netloc)


if __name__ == '__main__':
    # test_generate_url
    commPath = [
        "127.0.0.1:5000",
        "tools.test.com",
        "AutoTest",
        "ABCD.12345.FILE"
    ]
    commParas = {
        'action': "DemoAction",
        "version": "2.0",
        "timestamp": "2019-01-01T15:34:00"
    }
    print(generate_url(*commPath, **commParas))
    # test_parse_url
    url = 'http://127.0.0.1:5000/tools.test.com/AutoTest/ABCD.12345.FILE?start=500&aa=222&end=150000&read=100&cdf=we2&skip=200&type=readskip'
    result = parse_url(url)
    print(result)
    # test_get_path_by_replace_host_port
    print(get_path_by_replace_host_port(url, '127.1.1.1:9999'))
    # test_get_host_port_with_prefix
    print(get_host_port_with_prefix(url))


