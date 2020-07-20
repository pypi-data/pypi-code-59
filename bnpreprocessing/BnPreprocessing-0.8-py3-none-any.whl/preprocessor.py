"""
Author = Kowsher Ahmed, Avishek Das,
Email = ahmedshuvo969@gmail.com, avishek.das.ayan@gmail.com
"""


from pathlib import Path
import re
script_location = Path(__file__).absolute().parent
sw_loc = script_location / "bn_stopwords.txt"

class BnPreprocessing:

    def __init__(self):
        with open(sw_loc,'r',encoding = 'utf-8') as f:
    		self.stop_words = f.read()

    def remove_punc(self,text):
        pattern = re.compile('[!@#$%‘’^“”&√*()_+-={}\[\];:\'\"\|<>,.///?`~।]', flags=re.I)
        return pattern.sub(r'', text).replace("\\", "") 

    def remove_nonBangla(self,text):
        pattern = re.compile('[A-Z]', flags=re.I)
        return pattern.sub(r'', text)

    def remove_emoticons(self,text):
        regrex_pattern = re.compile(pattern = "["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags = re.UNICODE)
        return regrex_pattern.sub(r'',text)
    
    def remove_sw(self,text):
        x1 = [i for i in  text.split() if i not in self.stop_words]
        return ' '.join([i for i in x1])

    def remove_noise(self,text):
    	return self.remove_sw(self.remove_emoticons(self.remove_nonBangla(self.remove_punc(text))))