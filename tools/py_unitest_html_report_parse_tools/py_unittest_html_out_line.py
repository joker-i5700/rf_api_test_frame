# -*- coding: utf-8 -*-
"""
!/usr/bin/python3
@CreateDate   : 2019-07-18
@Author      : jet
@Filename : py_unittest_html_out_line.py
@Software : pycharm
"""

import os
from HTMLParser import HTMLParser


class PyUnittestHtmlParser(HTMLParser):
    """解析PyUnittestHtml报告，生成一个概要信息的html，放于邮件报告展示"""

    def __init__(self):
        HTMLParser.__init__(self)
        self._infos = {}
        self._failTestcase = []
        self._startParsePrimary = False
        self._startParseFail = False
        self._startParseSuccess = False
        self._startParseInfo = False
        self._failcase = False
        self._startParseTestcase = False

    def handle_starttag(self, tag, attrs):
        # print("in handle_starttag")
        if tag == 'a':
            print(attrs)
            if ('class', 'btn btn-primary') in attrs:
                self._startParsePrimary = True
            elif ('class', 'btn btn-danger') in attrs:
                self._startParseFail = True
            elif ('class', 'btn btn-success') in attrs:
                self._startParseSuccess = True
            elif ('class', 'btn btn-info') in attrs:
                self._startParseInfo = True
            else:
                self._startParsePrimary = False
                self._startParseFail = False
                self._startParseSuccess = False
                self._startParseInfo = False

        elif tag == 'td':
            if ('class', 'failCase') in attrs:
                self._failcase = True
        elif tag == 'div':
            if ('class', 'testcase') in attrs and self._failcase == True:
                self._startParseTestcase = True
                self._failcase = False
            else:
                self._startParseTestcase = False

    def handle_data(self, data):
        # print("in handle_data")
        if self._startParsePrimary:
            self._infos['primary'] = data[data.find('{') + 1:data.find('}')]
            self._startParsePrimary = False
        elif self._startParseFail:
            self._infos['fail'] = data[data.find('{') + 1:data.find('}')]
            self._startParseFail = False
        elif self._startParseSuccess:
            self._infos['success'] = data[data.find('{') + 1:data.find('}')]
            self._startParseSuccess = False
        elif self._startParseInfo:
            self._infos['info'] = data[data.find('{') + 1:data.find('}')]
            self._startParseInfo = False
        elif self._startParseTestcase:
            self._failTestcase.append(data)
            self._startParseTestcase = False

    def parse(self, filePath):
        print("---parse---")
        with open(filePath, 'r', encoding="utf-8") as fp:
            self.feed(fp.read())
            self.close()
        print("self._infos:{0}, self._failTestcase:{1}".format(self._infos, self._failTestcase))
        return self._infos, self._failTestcase


class PyUnittestHtmlOutLine(object):

    def __init__(self, pyUnittestHtmlFile, genareteReport='outline.html'):
        self._pyUnittestHtmlFile = pyUnittestHtmlFile
        self.genareteReport = genareteReport
        self._tableWidth = 800

    def genarete(self):
        infos, failTestcases = PyUnittestHtmlParser().parse(self._pyUnittestHtmlFile)
        self._genareteHtml(infos, failTestcases)

    def _genareteHtml(self, infos, failTestcases):
        strs = '''<html>
            <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
            <title>TotalResult</title>'''
        strs + '<body>'
        strs += self._generate_total_table_str(infos, failTestcases)
        strs += '</br><hr style="height:1px;border:none;border-top:1px solid #555555;" />'
        strs += self._generate_detail_failcase_str(failTestcases)
        strs += '</body></html>'
        self._write_to_html(strs)
        pass

    def _generate_total_table_str(self, infos, failTestcases):
        strs = '<table border="1"  cellspacing="0" width="{0}">'.format(self._tableWidth)
        tableHeaders = {'info': '所有', 'success': '成功', 'fail': '失败', 'primary': '通过率'}
        lists = ['info', 'success', 'fail', 'primary']
        headerValue = '<tr>'
        contentValue = '<tr>'
        for key in lists:
            headerValue += '<td align="center" bgcolor="{0}" width="200">{1}</td>'.format('#6699CC',
                                                                                          tableHeaders.get(key))
            if key == 'primary':
                failTestNum = len(failTestcases)
                bgColor = '#00A600' if failTestNum == 0 else '#FF0000'
                contentValue += '<td align="center" width="200" bgcolor="{1}">{0}</td>'.format(infos.get(key), bgColor)
            else:
                contentValue += '<td align="center" width="200">{0}</td>'.format(infos.get(key))
        headerValue += '</tr>'
        contentValue += '</tr>'
        strs += headerValue
        strs += contentValue
        strs += '</table>'
        return strs

    def _generate_detail_failcase_str(self, failTestcases):
        strs = '<table border="1"  cellspacing="0" width="{0}">'.format(self._tableWidth)
        firstRowFlag = False
        for failTest in failTestcases:
            strs += '<tr>'
            if not firstRowFlag:
                strs += '<td rowspan="{0}"  align="center" width="100">{1}</td>'.format(len(failTestcases), 'Fail Test')
                firstRowFlag = True
                print(failTest)
            strs += '<td  align="left">{0}</td>'.format(failTest)
            strs += '</tr>'
        strs += '</table>'
        return strs

    def _write_to_html(self, htmlContent):
        filePath = os.path.dirname(__file__) + '/' + self.genareteReport
        with open(filePath, 'w+', encoding="utf-8") as htmlFile:
            htmlFile.write(htmlContent)


if __name__ == '__main__':
    #     pyUnittestHtmlFile = sys.argv[1]
    #     PyUnittestHtmlOutLine(pyUnittestHtmlFile).genarete()
    PyUnittestHtmlOutLine('C:\\Users\\xl\\Documents\\rf_api_test_frame\\test\\unit\\unittest_report.html').genarete()

