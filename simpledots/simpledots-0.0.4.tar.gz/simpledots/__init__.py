'''
__init__.py: base file for simpledots
Lincoln Ombelets, 2020
'''

__version__ = '0.0.1'
__author__  = '''Lincoln Ombelets'''
__email__   = 'lombelets@caltech.edu'

from .simpledots import WBImage, DotImage, show_two_ims, coloc
from .utils import fetch_image
del simpledots