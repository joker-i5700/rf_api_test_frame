from .keywords import keywords
from .version import VERSION

_version_ = VERSION

class TestLibrary(keywords):
    '''
    Thunder RF TestLibrary. Generate by jet.
    
    You can execute   *python -m robot.libdoc -v docVersion ./TestLibrary/ TestLibrary.html*  command  to auto generate the doc.
    
    
    *Before running tests*

    Prior to running tests, TestLibrary must first be imported into your Robot test suite.

    Example:
        | Library | TestLibrary |

    
    '''
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'