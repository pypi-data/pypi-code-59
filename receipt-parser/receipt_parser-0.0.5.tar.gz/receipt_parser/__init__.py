__version__ = '0.0.5'
__license__ = 'MIT'

try:
    from .receipt_parser import RuleBased
    from .finder import Finder
    from .normalizer import Normalizer
except ModuleNotFoundError:
    from receipt_parser import RuleBased
    from finder import Finder
    from normalizer import Normalizer

