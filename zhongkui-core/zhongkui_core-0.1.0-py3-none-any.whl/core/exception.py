"""zhongkui exception"""


class ZhongkuiCriticalError(Exception):
    """zhongkui critical error"""


class ZhongkuiParseError(ZhongkuiCriticalError):
    """zhongkui parse error"""


class ZhongkuiInvalidFile(ZhongkuiCriticalError):
    """ zhongkui invalid file"""


class ZhongkuiUnpackError(ZhongkuiCriticalError):
    """zhongkui unpack error"""


class ZhongkuiApiError(ZhongkuiCriticalError):
    """Error during API usage."""