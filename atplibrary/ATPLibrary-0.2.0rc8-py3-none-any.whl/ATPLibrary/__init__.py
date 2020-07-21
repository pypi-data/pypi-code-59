from .ATPKeywords import ATPKeywords
from .version import __VERSION__

__VERSION__ = __VERSION__

class ATPLibrary(ATPKeywords):
    """``ATPLibrary`` is a ATP keyword library that uses
    test library that uses the [https://github.com/kennethreitz/requests|Requests] HTTP client.
    Here is a sample test case:
    | ***** Settings *****   |                                 |                     |                       |               |
    | Library                | Collections                     |                     |                       |               |
    | Library                | ATPLibrary                      |                     |                       |               |
    | ***** Test Cases ***** |                                 |                     |                       |               |
    | Till Transaction       |                                 |                     |                       |               |
    |                        | Perform Ping                    |                     |                       |               |
    """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = __VERSION__