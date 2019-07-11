from .Persistence import Persistence
from .Parse import RequestParse
from .Parse import ExcelParse
from .algorithm import crypt

class keywords(Persistence, RequestParse, ExcelParse, crypt):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'