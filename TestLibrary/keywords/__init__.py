from .algorithm import crypt
from .Parse import RequestParse
from .Parse import ExcelParse
from .Parse import UrlParse
from .Parse import KwDataTypeUtility
from .Persistence import Persistence

class keywords(Persistence, RequestParse, ExcelParse, UrlParse, KwDataTypeUtility, crypt):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'