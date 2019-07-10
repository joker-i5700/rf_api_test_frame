# -*- coding: utf-8 -*-
"""
!/usr/bin/python3
@CreateDate   : 2019-02-28
@Author      : jet
@Filename : ExcelParse.py
@Software : eclipse + RED
"""

'''  
                   导入操作excel需要第三方的xlrd Library
'''
import xlrd
from xlrd import open_workbook, cellname, xldate_as_tuple, \
    XL_CELL_NUMBER, XL_CELL_DATE, XL_CELL_TEXT, XL_CELL_BOOLEAN, \
    XL_CELL_ERROR, XL_CELL_BLANK, XL_CELL_EMPTY, error_text_from_code
from robot.api import logger

class ExcelParse:
    def __init__(self):
        self.wb = None
        self.tb = None
        self.sheetNum = None
        self.sheetNames = None
        self.fileName = None

    def kw_open_excel(self, filename):
        """
                        说明：从“文件名”参数中提供的路径打开Excel文件。
                         
                         参数:
                |  File Name (string)                      | 将用于打开Excel文件以执行测试的文件名字符串值。                                  |
                        例子:

        | *Keywords*           |  *Parameters*                                      |
        | Open Excel           |  C:\\Python27\\ExcelRobotTest\\ExcelRobotTest.xls  |

        """
        try:
            self.wb = xlrd.open_workbook(filename,encoding_override='utf-8')
        except Exception as e:
            logger.error(e)
        self.fileName = filename
        self.sheetNames = self.wb.sheet_names()
            
    def kw_read_cell_data_by_name(self, sheetname, cell_name):
        """
                        说明：使用单元格名称从该单元格返回数据。

                        参数:
                |  Sheet Name (string)  | 单元格值将从中返回的所选工作表。  |
                |  Cell Name (string)   | 将从中返回值的选定单元格名称。   |
                
                        返回值：
                |  return value (String)                      | 返回单元格数据        |
                        例子:

        | *Keywords*           |  *Parameters*                                             |
        | Open Excel           |  D:\\Python37\\ExcelRobotTest\\ExcelRobotTest.xls  |      |
        | Get Cell Data        |  TestSheet1                                        |  A2  |

        """ 
        my_sheet_index = self.sheetNames.index(sheetname)
        sheet = self.wb.sheet_by_index(my_sheet_index)
        for row_index in range(sheet.nrows):
            for col_index in range(sheet.ncols):
                cell = cellname(row_index, col_index)
                if cell_name == cell:
                    cellValue = sheet.cell(row_index, col_index).value
        return cellValue
    

    
    
    
    
    
    
    
    