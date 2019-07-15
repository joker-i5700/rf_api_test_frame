from .RequestParse import RequestParse
from .ExcelParse import ExcelParse
from .UrlParse import UrlParse

class Parse(RequestParse, ExcelParse, UrlParse):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'