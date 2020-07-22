from .auth import auth_user,set_id

__version__ = '0.1.3'

name, target_id = auth_user()
#from .bot import bot
from .core import *
