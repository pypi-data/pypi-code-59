"""zhongkui core package"""
from .file import File
from .parse import exiftool
from .corpus import FILETYPE
from .exception import ZhongkuiParseError, ZhongkuiInvalidFile


__version__ = "0.1.0"
