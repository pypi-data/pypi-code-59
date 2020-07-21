import re

class Syllable:
    """
    It takes advantage of hindi syllable separation from Pandey here: https://pandey.github.io/posts/tokenize-indic-syllables-python.html
    """
    vowels = '\u0904-\u0914\u0960-\u0961\u0972-\u0977' 
    consonants = '\u0915-\u0939\u0958-\u095F\u0978-\u097C\u097E-\u097F' 
    glottal = '\u097D' 
    vowel_signs = '\u093E-\u094C\u093A-\u093B\u094E-\u094F\u0955-\u0957\u1CF8-\u1CF9' 
    nasals = '\u0900-\u0902\u1CF2-\u1CF6' 
    visarga = '\u0903' 
    nukta = '\u093C' 
    avagraha = '\u093D' 
    virama = '\u094D' 
    vedic_signs = '\u0951-\u0952\u1CD0-\u1CE1\u1CED' 
    visarga_modifiers = '\u1CE2-\u1CE8' 
    combining = '\uA8E0-\uA8F1' 
    om = '\u0950' 
    accents = '\u0953-\u0954' 
    dandas = '\u0964-\u0965' 
    digits = '\u0966-\u096F' 
    abbreviation = '\u0970' 
    spacing = '\u0971' 
    vedic_nasals = '\uA8F2-\uA8F7\u1CE9-\u1CEC\u1CEE-\u1CF1' 
    fillers = '\uA8F8-\uA8F9' 
    caret = '\uA8FA' 
    headstroke = '\uA8FB' 
    space = '\u0020' 
    joiners = '\u200C-\u200D'
    def __init__(self,string):
        self.string = string
    def _syllabify(self): 
        syllables = [] 
        curr = '' # iterate over each character in the input. if a char belongs to a # class that can be part of a syllable, then add it to the curr # buffer. otherwise, output it to syllables[] right away. 
        for char in self.string: 
            if re.match('[' + vowels + avagraha + glottal + om + ']', char): # need to handle non-initial independent vowel letters, # avagraha, and om 
                if curr != '': 
                    syllables.append(curr) 
                    curr = char 
                else: 
                    curr = curr + char 
            elif re.match('[' + consonants + ']', char): # if last in curr is not virama, output curr as syllable # else add present consonant to curr 
                if len(curr) > 0 and curr[-1] != virama: 
                    syllables.append(curr) 
                    curr = char 
                else: curr = curr + char 
            elif re.match('[' + vowel_signs + visarga + vedic_signs + ']', char): 
                curr = curr + char 
            elif re.match('[' + visarga_modifiers + ']', char): 
                if len(curr) > 0 and curr[-1] == visarga: 
                    curr = curr + char 
                    syllables.append(curr) 
                    curr = '' 
                else: 
                    syllables.append(curr) 
                    curr = '' 
            elif re.match('[' + nasals + vedic_nasals + ']', char): # if last in curr is a vowel sign, output curr as syllable # else add present vowel modifier to curr and output as syllable 
                vowelsign = re.match('[' + vowel_signs + ']$', curr) 
                if vowelsign: 
                    syllables.append(curr) 
                    curr = '' 
                else: 
                    curr = curr + char 
                    syllables.append(curr) 
                    curr = '' 
            elif re.match('[' + nukta + ']', char): 
                curr = curr + char 
            elif re.match('[' + virama + ']', char): 
                curr = curr + char 
            elif re.match('[' + digits + ']', char): 
                curr = curr + char 
            elif re.match('[' + fillers + headstroke + ']', char): 
                syllables.append(char) 
            elif re.match('[' + joiners + ']', char): 
                curr = curr + char 
            else: 
                pass #print ("unhandled: " + char + " ", char.encode('unicode_escape')) # handle remaining curr 
        if curr != '': 
            syllables.append(curr) 
            curr = '' # return each syllable as item in a list 
        return syllables
    def _getSyllables(self): 
        word_syllables = [] 
        all_words = [] 
        for word in self.string.split(): 
            word = word.strip() 
            word = re.sub('[\s\n\u0964\u0965\.]', '', word) 
            word_syllables = Syllable(self.string)._syllabify() #number_syllables = len(word_syllables) #joined_syllables = '\u00B7'.join(word_syllables) 
            joined_syllables = word_syllables # make list of lists containing each word #all_words.append([word, joined_syllables, number_syllables]) 
            all_words.append([word, joined_syllables]) 
        return all_words    
class Hindi:
    """
    As the paper uses the text ranging from 400-1000 words so I normalize the formula of number of pollysyllables accordingly 
    """ 
    def __init__(self, string):
        self.string = string 
    def _words(self):
        for c in (":",".",",","!","'?"):
            string = self.string.replace(c,"")
        return Syllable(string)._getSyllables()
    def _awl(self):
        words = Hindi(self.string)._words()   
        words = [len(word[0]) for word in words if word[1]!=[]]
        return round(sum(words)/len(words),0)
    def _psw(self):
        words = Hindi(self.string)._words()  
        pollywords = [len(word[1]) for word in words if len(word[1])>2]
        if len(words)>1000:
            psw = len(pollywords)/len(words)*1000
        elif len(words)<400:
            psw = len(pollywords)/len(words)*400
        else:
            psw = len(pollywords)       
        return psw
    def score(self):
        return round(-2.34+2.14*Hindi(self.string)._awl()+0.01*Hindi(self.string)._psw(),0)