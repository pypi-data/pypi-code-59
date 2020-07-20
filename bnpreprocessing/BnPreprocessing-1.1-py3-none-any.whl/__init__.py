"""
Author = Kowsher Ahmed, Avishek Das,
Email = ahmedshuvo969@gmail.com, avishek.das.ayan@gmail.com
"""


from pathlib import Path
script_location = Path(__file__).absolute().parent
sw_loc = script_location / "bn_stopwords.txt"
with open(sw_loc,'r',encoding = 'utf-8') as f:
    stop_words = f.read()

import re

def remove_punc(text):
    pattern = re.compile('[1234567890১২৩৪৫৬৭৮৯০!@#$%‘’^“”&√*()_+-={}\[\];:\'\"\|<>,.///?`~।]', flags=re.I)
    return pattern.sub(r' ', text).replace("\\", "") 

def remove_nonBangla(text):
    pattern = re.compile('[A-Z]', flags=re.I)
    return pattern.sub(r'', text)

def remove_emoticons(text):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)

def remove_sw(text):
    x1 = [i for i in  text.split() if i not in stop_words]
    return ' '.join([i for i in x1])

def remove_noise(text):
    return remove_sw(remove_emoticons(remove_nonBangla(remove_punc(text))))