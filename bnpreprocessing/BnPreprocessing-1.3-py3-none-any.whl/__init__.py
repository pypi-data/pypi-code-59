from pathlib import Path
script_location = Path(__file__).absolute().parent
sw_loc = script_location / "bn_stopwords.txt"
with open(sw_loc,'r',encoding = 'utf-8') as f:
    stop_words = f.read()

import re
from .processing import *