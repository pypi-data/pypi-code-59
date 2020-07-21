import pandas as pd
import numpy as np
import random
import pickle
import string
import time
import logging
import urllib.parse
import re
import datetime
from datetime import timezone
from pandas.api.types import is_string_dtype, is_numeric_dtype
from collections import Counter

eapl_kpi_logger = logging.getLogger('search_err ')
logger_prc = logging.getLogger('data_preprocessing_prc_req')

#TODO: Add Performance logging
class eapl_kpi:
	def eapl_convert_to_list(x):
	    return x if isinstance(x, list) else [x]


	            

