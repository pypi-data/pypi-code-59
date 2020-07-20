"""
emoji for Python
~~~~~~~~~~~~~~~~

emoji terminal output for Python.

    >>> from TextProcess_bak import emoji
    >>> print(emoji.emojize('Python is :thumbsup:', use_aliases=True))
    Python is 👍
    >> print(emoji.emojize('Python is :thumbs_up:'))
    Python is 👍
"""

from TextProcess_bak.emoji.unicode_codes import EMOJI_ALIAS_UNICODE
from TextProcess_bak.emoji.unicode_codes import EMOJI_UNICODE
from TextProcess_bak.emoji.unicode_codes import UNICODE_EMOJI
from TextProcess_bak.emoji.unicode_codes import UNICODE_EMOJI_ALIAS

from TextProcess_bak.emoji.core import *