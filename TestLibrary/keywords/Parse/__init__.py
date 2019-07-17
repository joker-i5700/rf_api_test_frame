from .RequestParse import RequestParse
from .ExcelParse import ExcelParse
from .UrlParse import UrlParse
from .DataTypeUtility import KwDataTypeUtility

class Parse(RequestParse, ExcelParse, UrlParse, KwDataTypeUtility):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'