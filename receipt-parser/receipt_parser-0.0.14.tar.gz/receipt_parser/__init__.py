__version__ = '0.0.14'
__license__ = 'MIT'


from .receipt_parser import RuleBased
from .finder import Finder
from .normalizer import Normalizer

# try:
#     from .receipt_parser import RuleBased
#     from .finder import Finder
#     from .normalizer import Normalizer
# except ModuleNotFoundError:
#     from receipt_parser import RuleBased
#     from finder import Finder
#     from normalizer import Normalizer

