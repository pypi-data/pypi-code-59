"""
Implement formula SPIKE 
"""

import re
class Bahasa:
    """
    Implement SPIKE formula 
    """
    def __init__(self, string: str):
        self.string=string
    def _sentences(self):
        string = self.string
        return len(re.split(r'[.!?]+', string))
    def _words(self):
        words = string.split()
        words = [re.sub('[^a-zA-Z]+', '', word) for word in words]
        words = [word for word in words if word !='']
        return len(words)
    def _syllables(self): 
        syllable_count = 0
        vowels = 'aeiouy'
        words = string.split(' ')
        words = [re.sub('[^a-zA-Z]+', '', word) for word in words]
        words = [word for word in words if word !='']
        for word in words: 
            if word[0] in vowels:
                syllable_count += 1
            if len(word) >=2:
                for index in range(1, len(word)):
                    if word[index] in vowels and word[index - 1] not in vowels:
                        syllable_count += 1
            if word.endswith('e'):
                syllable_count -= 1
            if word.endswith('le') and len(word) > 2 and word[-3] not in vowels:
                syllable_count += 1
            if syllable_count == 0:
                syllable_count += 1
        return syllable_count
    def _diffword(self):
        kg = string.count('kata ganda')
        dt = string.count('diftong')
        kp = string.count('kata Pinjaman')
        kh = string.count('kekeliruan huruf')
        return (kg+dt+kp+kh)
    def spike(self):
        a = -13.988
        b = 0.3793
        c=0.0207
        n = Bahasa(self.string)._words()/Bahasa(self.string)._sentences()
        d = Bahasa(self.string)._syllables()*300/Bahasa(self.string)._words()
        k = Bahasa(self.string)._diffword()*300/Bahasa(self.string)._words()
        return round(a+b*n+c*(d+k*5),0)


    