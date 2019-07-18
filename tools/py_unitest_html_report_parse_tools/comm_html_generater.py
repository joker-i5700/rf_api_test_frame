# -*- coding: utf-8 -*-
"""
!/usr/bin/python3
@CreateDate   : 2019-07-18
@Author      : jet
@Filename : comm_html_generater.py
@Software : eclipse + pydev
"""


class htmlGenerate(object):

    tagAttrDict = {
        "global": ["accesskey", "class", "contenteditable", "id", "hidden", "lang", "spellchenk", "style", "title"],
        "table": ["align", "bgcolor", "border", "cellpadding", "cellspacing", "frame", "rules", "summary", "width"],
        "tr": ["align", "bgcolor", "char", "charoff", "valign"],
        "td": ["abbr", "align", "axis", "bgcolor", "char", "colspan", "headers", "height", "nowrap", "rowspan", "scope", "valign", "width"]
    }

    def __init__(self, fileName="./output.html", title="TotalResult", meta='''http-equiv="Content-Type" content="text/html; charset=utf-8"'''):
        """
        :param title: table的title
        :param fileName: html文件写入的文件
        :return:
        """
        self.htmlStart = '''<html>\n\t<head>\n\t\t<meta {0}/>\n\t\t<title>{1}</title>\n\t</head>\n\t<body>\n\t\t'''.format(meta, title)
        self.htmlEnd = '''\n\t</body>\n\t\t</html>'''
        self.htmlCentent = ""
        self.fileName = fileName

    class tableLine(object):

        def __init__(self, lineContentDict):
            attr = htmlGenerate()._attrHandle(lineContentDict[0].get("thisLineStyle")) if "thisLineStyle" in lineContentDict[0].keys() else ""
            self.lineStart = "<tr {0}>\n\t\t\t".format(attr)
            self.lineEnd = "</tr>\n\t\t"
            self.lineContent = ""
            for columnNum in range(len(lineContentDict)):
                self.lineContent += self._getColumn(lineContentDict[columnNum])

        def getLineStr(self):
            return self.lineStart + self.lineContent + self.lineEnd

        def _getColumn(self, columnDict):
            """
                                    生成table中的<td>
            :param columnDict: 形如{"processNum":{"align":"center", "bgcolor":"white"}，其中字典的key为<td>内容，
            value为td的指定属性
            :return:
            """
            columnStr = ""
            for cellContent, cellAttr in columnDict.items():
                attr = htmlGenerate()._attrHandle(cellAttr, "td")
                if not attr:
                    attr = '''colspan="1" align="center" width="800" bgcolor="white"'''
                columnStr += '''<td {0}>{1}</td>\n\t\t\t'''.format(attr, cellContent)
            return columnStr

    def addTable(self, tableDataDict,tableAttrDict=None):
        """
                        添加html中的table
        :param tableDataDict:table数据列表，二维数组的每个元素为表格中的一个单元格(用字典表示，字典的key为单元格的值，字典的value为单元格属性组成的字典)，形如  、
        [
           [
            {'ProjectName': {'bgcolor': '#6699CC', 'width': '200'}},
            {'Total': {'bgcolor': '#FFFFAA', 'width': '150'}},
          ],
          [
            {'OSS_ST_Autotest': {'bgcolor': '#97CBFF', 'align': 'left'}},
            {'170': None}
          ],
          [
            {'Transcode_ST_Autotest': {'bgcolor': '#97CBFF', 'align': 'left'}},
            {'183': None}
          ]
        ]
        :param tableAttrDict:<table>标签的属性组成的字典
        :return:
        """
        attr = self._attrHandle(tableAttrDict, "table")
        if not attr:
            attr = '''border="1"  cellspacing="0" width="800"'''
        table = '<table {0}>'.format(attr)
        for lineNum in range(len(tableDataDict)):
            table += self.tableLine(tableDataDict[lineNum]).getLineStr()
        table += '</table>\n\t\t'
        self.htmlCentent += table

    def addBr(self, attrDict=None):
        """
                        添加html换行标签
        :param attrDict: br标签的属性组成的字典
        :return:
        """
        attrStr = self._attrHandle(attrDict)
        self.htmlCentent += "<br {0}/>".format(attrStr)

    def addHr(self, attrDict=None):
        """
                        添加html hr标签
        :param attrDict: hr标签属性组成的字典
        :return:
        """
        attr = self._attrHandle(attrDict)
        self.htmlCentent += "<hr {0}/>".format(attr)

    def addHeader(self, content="a headline", level=3, attrDict=None):
        """
                        增加html标题,<h1> 定义最大的标题。<h6> 定义最小的标题。
        :param content:标题的内容
        :param level:标题大小
        :return:
        """
        if int(level) < 1 or int(level) > 6:
            logger.info("header level shou be within 1-6")
            return
        attrStr = self._attrHandle(attrDict)
        headline = '''<h{0} {1}>{2}</h{0}>'''.format(level, attrStr, content)
        self.htmlCentent += headline

    def _attrHandle(self, attrDict, attrKeyList="global"):
        attrStr = ""
        if attrDict:
            for attrKey, attrValue in attrDict.items():
                if attrKey in self.tagAttrDict[attrKeyList]:
                    attrStr += '''{0}="{1}" '''.format(attrKey, attrValue)
                else:
                    logger.info("{0} not in {1}".format(attrKey, self.tagAttrDict[attrKeyList]))
        return attrStr

    def __del__(self):
        with open(self.fileName, "w", encoding="utf-8") as f:
            f.write(self.htmlStart + self.htmlCentent + self.htmlEnd)

if __name__ == "__main__":
    # dic = [
    #     [  # 表格第一行
    #         {"thisLineStyle": {"valign": "top", "align": "center", "bgcolor": "yellow"}},
    #         {"processNum": {"align": "center", "bgcolor": "blue"}},  # 表格第一行第一列
    #         {"total": {"bgcolor": "yellow"}},
    #         {"Success": {"bgcolor": "yellow"}},
    #         {"Fail": {"bgcolor": "yellow"}},
    #         {"SuccessRate": {"bgcolor": "yellow"}}
    #     ],
    #     [
    #         {"ST_OSS": {"align": "left", "bgcolor": "blue"}},
    #         {"200": None},
    #         {"4234": None},
    #         {"43": None},
    #         {"45.6": None}
    #     ]
    # ]
    dic = [[{'ProjectName': {'bgcolor': '#6699CC', 'width': '200'}}, {'Total': {'bgcolor': '#FFFFAA', 'width': '150'}}, {'Success': {'bgcolor': '#FFFFAA', 'width': '150'}}, {'Fail': {'bgcolor': '#FFFFAA', 'width': '150'}}, {'SuccessRate': {'bgcolor': '#FFFFAA', 'width': '150'}}], [{'OSS_ST_Autotest': {'bgcolor': '#97CBFF', 'align': 'left'}}, {'170': None}, {'169': None}, {'1': None}, {'''<a href="http://127.0.0.1:8080/job/OSS_ST_Autotest">99.41%</a>''': {'bgcolor': '#FF0000'}}], [{'All_API_MT_Autotest': {'bgcolor': '#97CBFF', 'align': 'left'}}, {'200': None}, {'200': None}, {'0': None}, {'''<a href="http://127.0.0.1:8080/job/All_API_MT_Autotest">100.0%</a>''': {'bgcolor': '#00BB00'}}], [{'Transcode_ST_Autotest': {'bgcolor': '#97CBFF', 'align': 'left'}}, {'183': None}, {'143': None}, {'40': None}, {'''<a href="http://127.0.0.1:8080/job/Transcode_ST_Autotest">78.14%</a>''': {'bgcolor': '#FF0000'}}], [{'XYCDN_ST_Autotest': {'bgcolor': '#97CBFF', 'align': 'left'}}, {'24': None}, {'24': None}, {'0': None}, {'''<a href="http://127.0.0.1:8080/job/XYCDN_ST_Autotest">100.0%</a>''': {'bgcolor': '#00BB00'}}], [{'PlatinumPlugin_ST_Autotest': {'bgcolor': '#97CBFF', 'align': 'left'}}, {'36': None}, {'35': None}, {'1': None}, {'''<a href="http://127.0.0.1:8080/job/PlatinumPlugin_ST_Autotest">97.22%</a>''': {'bgcolor': '#FF0000'}}]]
    dic1 = [[{'ttttt': {'bgcolor': '#6699CC', 'width': '200'}}, {'hhhh': {'bgcolor': '#FFFFAA', 'width': '150'}}, {'aa': {'bgcolor': '#FFFFAA', 'width': '150'}}, {'Fail': {'bgcolor': '#FFFFAA', 'width': '150'}}, {'SuccessRate': {'bgcolor': '#FFFFAA', 'width': '150'}}], [{'OSS_ST_Autotest': {'bgcolor': '#97CBFF', 'align': 'left'}}, {'170': None}, {'169': None}, {'1': None}, {'''<a href="http://127.0.0.1:8080/job/OSS_ST_Autotest">99.41%</a>''': {'bgcolor': '#FF0000'}}], [{'All_API_MT_Autotest': {'bgcolor': '#97CBFF', 'align': 'left'}}, {'200': None}, {'200': None}, {'0': None}, {'''<a href="http://127.0.0.1:8080/job/All_API_MT_Autotest">100.0%</a>''': {'bgcolor': '#00BB00'}}], [{'Transcode_ST_Autotest': {'bgcolor': '#97CBFF', 'align': 'left'}}, {'183': None}, {'143': None}, {'40': None}, {'''<a href="http://127.0.0.1:8080/job/Transcode_ST_Autotest">78.14%</a>''': {'bgcolor': '#FF0000'}}], [{'XYCDN_ST_Autotest': {'bgcolor': '#97CBFF', 'align': 'left'}}, {'24': None}, {'24': None}, {'0': None}, {'''<a href="http://127.0.0.1:8080/job/XYCDN_ST_Autotest">100.0%</a>''':{'bgcolor': '#00BB00'}}], [{'PlatinumPlugin_ST_Autotest': {'bgcolor': '#97CBFF', 'align': 'left'}}, {'36': None}, {'35': None}, {'1': None}, {'''<a href="http://127.0.0.1:8080/job/PlatinumPlugin_ST_Autotest">97.22%</a>''': {'bgcolor': '#FF0000'}}]]
    dic2 = [[{'OSS_ST_Autotest(Fail_Num:1)': {'bgcolor': '#97CBFF', 'align': 'left'}}, {'<a href="http://192.168.116.122:8080/job/OSS_ST_Autotest">detail</a>': None}], [{'Fail Test': {'rowspan': '1'}}, {'1Edge_1Origin_1Forward.Switch_Master_Slave.\xe6\x8e\xa8\xe6\xb5\x81\xe4\xb8\xbb\xe5\xa4\x87\xe5\x88\x87\xe6\x8d\xa2\xe4\xb8\xba\xe5\x8f\x8c\xe6\x8e\xa8': {'align': 'left'}}]]
    dict = [('OSS_ST_Autotest', 1, 169, [u'1Edge_1Origin_1Forward.Switch_Master_Slave.\u63a8\u6d41\u4e3b\u5907\u5207\u6362\u4e3a\u53cc\u63a8']), ('All_API_MT_Autotest', 0, 200, []), ('Transcode_ST_Autotest', 0, 183, []), ('XYCDN_ST_Autotest', 0, 24, []), ('PlatinumPlugin_ST_Autotest', 0, 36, [])]
    instance = htmlGenerate()
    instance.addTable(dic)
    instance.addBr()
    instance.addHr()
    instance.addTable(dic1)