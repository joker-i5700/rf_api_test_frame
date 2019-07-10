from .MysqlService import MysqlService
from .ConfigService import ConfigService

class Persistence(MysqlService, ConfigService):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'