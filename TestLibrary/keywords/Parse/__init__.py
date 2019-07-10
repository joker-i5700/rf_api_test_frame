from .RequestParse import RequestParse
from .ExcelParse import ExcelParse

class Parse(RequestParse,ExcelParse):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'