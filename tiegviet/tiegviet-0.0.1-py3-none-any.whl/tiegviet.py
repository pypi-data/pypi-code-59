import re
def convert_to_tiegviet(text):
    patterns = {
    #     Ordering of patterns is matter!!
        'kh':'x',
        'Kh':'X',
        'c(?!h)':'k',
        'q':'k',
        'd':'z', 
        'đ':'d',
        'gi':'z',    
        'ngh?':'q',
        'gh':'g',
        'nh':'n\'',
        'ph':'f',
        'ch':'c',
        'tr':'c',    
        'th':'w',

        'Gi':'Z',    
        'Ngh?':'Q',
        'Gh':'G',
        'Nh':'N\'',
        'Ph':'F',
        'Ch':'C',
        'Tr':'C',    
        'Th':'W',

        'r':'z',
    }
    
    output = text
    for regex, replace in patterns.items():
        output = re.sub(regex, replace, output)
        # deal with upper case
        output = re.sub(regex.upper(), replace.upper(), output)
    return output