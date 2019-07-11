# -*- coding: utf-8 -*-
"""
!/usr/bin/python3
@CreateDate   : 2019-02-27
@Author      : jet
@Filename : demo_generate_script.py
@Software : eclipse + RED
"""

import os
import xlrd
import re

def find_file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):  
        print ("当前目录路径",root)                   #当前目录路径  
        print ("当前路径下所有子目录",dirs)           #当前路径下所有子目录  
        print ("当前路径下所有非目录子文件",files)    #当前路径下所有非目录子文件
        files.sort()                          #排序后输出，使接口脚本按顺序生成
    return files

def openXls(file_name):
    xlsfile = r"./Demo_TestCase/" + file_name    # 打开指定路径中的xls文件
    return xlrd.open_workbook(xlsfile,encoding_override='utf-8')      #得到Excel文件的book对象，实例化对象

def readXlsSheet(xlsObj,count):
    sheet = xlsObj.sheet_by_index(count)         # 通过sheet索引获得sheet对象
    return xlsObj.sheet_names()[count]           # 获得指定索引的sheet表名字

def readXlsParameter(xlsObj,sheet_name):
    li = []
    sheet = xlsObj.sheet_by_name(sheet_name)     # 通过sheet名字来获取
    nrows = sheet.nrows                         # 获取行总数
    print ("nrows:",nrows)
    for i in range(1,nrows):
        print ("Parameter:",sheet.cell_value(i,0))
        li.append(sheet.cell_value(i,0))       #获取指定EXCEL文件中，第一个SHEET中的接口字段名
    return li

def readXlsMsgType(xlsObj):
    sheet = xlsObj.sheet_by_name('Case01')
    return sheet.cell_value(1,3)    #获取测试用例XLS表'Case01'SHEET中'D2'字段内容

def readXlsType(xlsObj):
    sheet = xlsObj.sheet_by_name('Case01')
    return sheet.cell_value(1,6)    #获取测试用例XLS表'Case01'SHEET中'G2'字段内容

def readXlsUrl(xlsObj):
    sheet = xlsObj.sheet_by_name('Case01')
    return sheet.cell_value(1,7)    #获取测试用例XLS表'Case01'SHEET中'H2'字段内容

def readXlsGroup(xlsObj):
    sheet = xlsObj.sheet_by_name('Case01')
    return sheet.cell_value(1,8)    #获取测试用例XLS表'Case01'SHEET中'I2'字段内容

def readXlsSummary(xlsObj):
    sheet = xlsObj.sheet_by_name('Case01') 
    return sheet.cell_value(1,9)   #获取测试用例XLS表'Case01'SHEET中'J2'字段内容

def readXlsHeaders(xlsObj):
    sheet = xlsObj.sheet_by_name('Case01') 
    return sheet.cell_value(1,10)   #获取测试用例XLS表'Case01'SHEET中'K2'字段内容

def GeneratekwExcel_init(fileName):
    if os.path.exists(fileName):
        os.remove(fileName)
    f = open(fileName,'a')
 
    f.write('*** Settings ***' + '\n')
    f.write('Library           TestLibrary' + '\n')
    f.write('\n')
    f.write('*** Keywords ***' + '\n')

    f.close()

def kwRequests_init(fileName):
    if os.path.exists(fileName):
        os.remove(fileName)
    f = open(fileName, 'a')

    f.write('*** Settings ***' + '\n')
    f.write('Library           TestLibrary' + '\n')
    f.write('Library           RequestsLibrary' + '\n')
    f.write('\n')
    f.write('*** Keywords ***' + '\n')

    f.close()

def InterfaceTestCase_init(fileName):
    if os.path.exists(fileName):
        os.remove(fileName)
    f = open(fileName, 'a')
    f.write('*** Settings ***' + '\n')
    f.write('Suite Setup       Log    Suite Setup' + '\n')
    f.write('Suite Teardown    Log    Suite Teardown' + '\n')
    f.write('Test Setup        log    Test Setup' + '\n')
    f.write('Test Teardown     log    Teardown' + '\n')
    f.write('Resource          Demo_kwRequests.robot' + '\n')
    f.write('Resource          Demo_kwExcel.robot' + '\n')
    f.write('\n')

    f.write('*** Variables ***' + '\n')
    f.write('${IP_PORT}     http://127.0.0.1:5000' + '\n')
    f.write('\n')

    f.write('*** Test Cases ***' + '\n')


def GeneratekwExcel(fileName,Keys):
    f = open(fileName,'a')
    iKey = 2
    if '' != Keys[0].strip():  # 接口输入参数个数不为零
        for key in Keys:
            f.write('    ${' + key + '}    kw Read Cell Data By Name    ${CaseNo}    B' + str(iKey) + '\n')
            iKey = iKey + 1
    f.write('    ${ExpValue}    kw Read Cell Data By Name    ${CaseNo}    F2' + '\n')
    f.write('    [Return]')
    if '' != Keys[0].strip():  # 接口输入参数个数不为零
        for key in Keys:
            f.write('    ${' + key + '}')
    f.write('    ${ExpValue}' + '\n')
    f.write('\n')
    f.close()

def GeneratekwRequests(fileName,Keys,testCaseFileName,iType,iUrl,iSummary,iHeaders,iMsgType):
    
    hKeys = re.findall('\${(.+?)}',iHeaders)  #取出header中需要输入的变量
    urlKeys = re.findall('\${(.+?)}',iUrl)    #取出URL中需要输入的变量
    
    f = open(fileName,'a', encoding="utf-8")
    f.write('    [Arguments]    ${url}')
    if '' != Keys[0].strip():  # 接口输入参数个数不为零
        for key in Keys:
            f.write('    ${' + key + '}')
            
    #传入变量 做为URL，每次消息发送都会变化        
    if len(urlKeys):
        for key in urlKeys:
            f.write('    ${' + key + '}') 
                   
    #传入变量 做为HEADER，每次消息发送都会变化        
    if len(hKeys):
        for key in hKeys:
            f.write('    ${' + key + '}')
    
    f.write('\n')
    
    f.write('    [Documentation]   ' + iSummary + '\n')
    
    if "multipart/form-data" == iMsgType:
        f.write('    ${boundary}=    xl boundary parse    ${data}' + '\n')

    f.write('    ${headers}    Create Dictionary    ' + iHeaders + '\n')
    f.write('    Create Session    api    ${url}    ${headers}   verify=${False}' + '\n')

    if '' != Keys[0].strip():    # 接口输入参数个数不为零
        if iType.upper() == 'GET':
            f.write('    ${Ret}    Get Request   api   ' + iUrl)
            if "json_data" == Keys[0]:    #第一个KEY值为“json_data”表示GET请求带BODY体发送
                for key in Keys:
                    f.write('    json' + '=${' + key + '}')
            else:
                for key in Keys:
                    f.write('${' + key + '}')      #发送GET请求，直接把EXCEL中读取出来的参数连接到URL后面
            f.write('\n')
        elif iType.upper() == 'POST':
            f.write('    ${Ret}    Post Request   api   ' + iUrl)
            for key in Keys:
                f.write('    ' + key + '=${' + key + '}')
            f.write('\n')
        elif iType.upper() == 'DELETE':
            f.write('    ${Ret}    Delete Request   api   ' + iUrl)
            for key in Keys:
                f.write('    ' + key + '=${' + key + '}')
            f.write('\n')
        elif iType.upper() == 'PUT':
            f.write('    ${Ret}    Put Request   api   ' + iUrl)
            for key in Keys:
                f.write('${' + key + '}')
            f.write('\n')
        else:
            f.write('    ${Ret}    Post Request   api   ' + iUrl)
            for key in Keys:
                f.write('    ' + key + '=${' + key + '}')
            f.write('\n')
    else:
        if iType.upper() == 'GET':
            f.write('    ${Ret}    Get    ${url}    headers=${headers}' + '\n')
        elif iType.upper() == 'POST':
            f.write('    ${Ret}    Post    ${url}    headers=${headers}' + '\n')
        elif iType.upper() == 'DELETE':
            f.write('    ${Ret}    Put    ${url}    headers=${headers}' + '\n')
        elif iType.upper() == 'PUT':
            f.write('    ${Ret}    Put    ${url}    params=${params}    headers=${headers}' + '\n')
        else:
            f.write('    ${Ret}    ' + iType + '    ${url}    headers=${headers}' + '\n')

    f.write('    [Return]    ${Ret}' + '\n')

    f.write('\n')
    f.close()

def GenerateInterfaceTestCase(fileName,Keys,testCaseFileName,tag):
    f = open(fileName, 'a')
    f.write('    [Tags]    ' + tag + '\n')
    if '' != Keys[0].strip():  # 接口输入参数个数不为零
        for key in Keys:
            f.write('    ${' + key + '}')
    f.write('    ${exp}    Demo_Get_' + testCaseFileName[:-4] + '_Parameters    Case01')
    f.write('\n')
    f.write('    ${Resp_data}    Demo_' + testCaseFileName[:-4] + '    ${IP_PORT}')
    if '' != Keys[0].strip():  # 接口输入参数个数不为零
        for key in Keys:
            f.write('    ${' + key + '}')
    f.write('\n')
    f.write('    Log    ${Resp_data.text}' + '\n')
    f.write('    Should Be Equal As Strings    ${Resp_data.status_code}    200' + '\n')
    f.write('    Should Be Equal    ${Resp_data.text}    ${exp}' + '\n')
    f.write('\n')
    f.close()

testCaseFiles = find_file_name("./Demo_TestCase")
print (len(testCaseFiles))
'''--------------生成kwExcel.robot脚本文件--------------'''
i = 0
kwExcel_name = 'Demo_kwExcel.robot'
GeneratekwExcel_init(kwExcel_name)

for caseName in testCaseFiles:
    f = open(kwExcel_name, 'a')
    f.write('Demo_Get_' + caseName[:-4] + '_Parameters' + '\n')
    f.write('    [Arguments]    ${CaseNo}' + '\n')
    f.write('    kw Open Excel    ${CURDIR}${/}Demo_TestCase${/}' + caseName + '\n')
    f.close()
    while i < len(testCaseFiles):
        book = openXls(testCaseFiles[i])
        print ("file name:",testCaseFiles[i])
        sheet_name = readXlsSheet(book,0)
        print ("sheet name:",sheet_name)
        pLi = readXlsParameter(book,sheet_name)
        print ("pLi:",pLi)
        GeneratekwExcel(kwExcel_name,pLi)
        break
    i = i+1

'''--------------生成kwRequests.robot脚本文件--------------'''
j = 0
kwRequests_name = 'Demo_kwRequests.robot'
kwRequests_init(kwRequests_name)

for caseName in testCaseFiles:
    f = open(kwRequests_name, 'a')
    f.write('Demo_' + caseName[:-4] + '\n')
    f.close()
    while j < len(testCaseFiles):
        bookRequests = openXls(testCaseFiles[j])
        print ("file name:",testCaseFiles[j])
        sheetNameReq = readXlsSheet(bookRequests,0)
        print ("sheet name:",sheetNameReq)
        pLiReq = readXlsParameter(bookRequests,sheetNameReq)
        print ("pLi:",pLiReq)
        typeName = readXlsType(bookRequests)
        print ("typeName:",typeName)
        urlValue = readXlsUrl(bookRequests)
        print ("urlValue:",urlValue)
        summaryValue = readXlsSummary(bookRequests)
        print ("summaryValue:",summaryValue)
        headersValue = readXlsHeaders(bookRequests)
        print("headersValue: ",headersValue)
        
        msgTypeValue = readXlsMsgType(bookRequests)
        print("msgTypeValue: ",msgTypeValue)
        GeneratekwRequests(kwRequests_name,pLiReq,testCaseFiles[j],typeName,urlValue,summaryValue,headersValue,msgTypeValue)
        break
    j = j+1

'''--------------生成InterfaceTestCaseDemo.robot脚本文件--------------'''
k = 0
InterfaceTestCase_name = 'Demo_InterfaceTestCaseDemo.robot'
InterfaceTestCase_init(InterfaceTestCase_name)

for caseName in testCaseFiles:
    f = open(InterfaceTestCase_name, 'a')
    f.write(caseName[:-4] + '.Case01' + '\n')
    f.close()
    while k < len(testCaseFiles):
        bookInterfaceTestCase = openXls(testCaseFiles[k])
        print ("file name:",testCaseFiles[k])
        sheetNameTestCase = readXlsSheet(bookInterfaceTestCase,0)
        print ("sheet name:",sheetNameTestCase)
        pLiTestCase = readXlsParameter(bookInterfaceTestCase,sheetNameTestCase)
        print ("pLiTestCase:",pLiTestCase)
        groupName = readXlsGroup(bookInterfaceTestCase)
        print ("groupName:",groupName)
        GenerateInterfaceTestCase(InterfaceTestCase_name,pLiTestCase,testCaseFiles[k],groupName)
        break
    k = k+1



