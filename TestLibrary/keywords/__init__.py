from .Persistence import Persistence
from .Parse import RequestParse
from .Parse import ExcelParse

class keywords(Persistence, RequestParse,ExcelParse):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'