# -*- coding: utf-8 -*-
"""
!/usr/bin/python3
@CreateDate   : 2019-07-18
@Author      : jet
@Filename : py_unittest_html_outline_with_html_generater.py
@Software : eclipse + pydev
"""

import sys, os
sys.path.append(os.path.abspath("../../"))
from HTMLParser import HTMLParser
from tools.py_unitest_html_report_parse_tools.comm_html_generater import htmlGenerate


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
        if tag =='a':
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

        elif tag=='td':
            if ('class', 'failCase') in attrs:
                self._failcase=True
        elif tag == 'div':
            if ('class', 'testcase') in attrs and self._failcase == True:
                self._startParseTestcase = True
                self._failcase=False
            else:
                self._startParseTestcase = False

    def handle_data(self, data):
        if self._startParsePrimary:
            self._infos['primary'] = data[data.find('{')+1:data.find('}')]
            print(data)
            self._startParsePrimary = False
        elif self._startParseFail:
            self._infos['fail'] = data[data.find('{')+1:data.find('}')]
            self._startParseFail = False
        elif self._startParseSuccess:
            self._infos['success'] = data[data.find('{')+1:data.find('}')]
            self._startParseSuccess = False
        elif self._startParseInfo:
            self._infos['info'] = data[data.find('{')+1:data.find('}')]
            self._startParseInfo = False
        elif self._startParseTestcase:
            self._failTestcase.append(data)
            self._startParseTestcase = False

    def parse(self, filePath):
        with open(filePath, 'r', encoding="utf-8") as fp:
            self.feed(fp.read())
            self.close()
        return self._infos, self._failTestcase


class PyUnittestHtmlOutLine(object):

    def __init__(self, pyUnittestHtmlFile, genareteReport='outline.html'):
        self._pyUnittestHtmlFile = pyUnittestHtmlFile
        self.genareteReport = genareteReport

    def genarete(self):
        filePath = os.path.dirname(__file__) + '/' + self.genareteReport
        infos, failTestcases = PyUnittestHtmlParser().parse(self._pyUnittestHtmlFile)
        htmlInstance = htmlGenerate(filePath)
        htmlInstance.addTable(self._generateTotalTableDataList(infos, failTestcases))
        htmlInstance.addBr()
        htmlInstance.addHr()
        htmlInstance.addTable(self._generateDetailFailcaseTableDataList(failTestcases))

    def _generateTotalTableDataList(self, infos, failTestcases):
        tableHeaders = {'info': '所有', 'success': '成功', 'fail': '失败', 'primary': '通过率'}
        lists = ['info', 'success', 'fail', 'primary']
        headerLineList = []
        contentLineList = []
        tableDataList = []
        for key in lists:
            headerLineList.append({tableHeaders.get(key): {"bgcolor": "#6699CC", "width": 200}})
            if key == 'primary':
                failTestNum = len(failTestcases)
                bgColor = '#00A600' if failTestNum == 0 else '#FF0000'
                contentLineList.append({infos.get(key): {"bgcolor": "{0}".format(bgColor), "width": 200}})
            else:
                contentLineList.append({infos.get(key): {"width": 200}})
        tableDataList.append(headerLineList)
        tableDataList.append(contentLineList)
        return tableDataList

    def _generateDetailFailcaseTableDataList(self, failTestcases):
        lineList = []
        tableDataList = []
        firstRowFlag = False
        for failTest in failTestcases:
            if not firstRowFlag:
                lineList.append({"Fail Test": {"width": 100, "rowspan": "{0}".format(len(failTestcases))}})
                firstRowFlag = True
            lineList.append({failTest: {"align": "left"}})
            tableDataList.append(lineList)
        return tableDataList


if __name__ == '__main__':
#     pyUnittestHtmlFile = sys.argv[1]
#     PyUnittestHtmlOutLine(pyUnittestHtmlFile).genarete()
    PyUnittestHtmlOutLine('C:\\Users\\xl\\Documents\\rf_api_test_frame\\test\\unit\\unittest_report.html').genarete()

