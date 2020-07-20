from pprint import pprint
from statistics import mean as metric
from functools import reduce
import operator

product = lambda array : reduce(operator.mul, array, 1)

def paragraph(words) :
    """
    Determines the 'squarest' format of a paragraph
    """
    char_max = len(" ".join(words))  # Max "Width"
    char_min = min(map(len,words))   # Min "Width"
#     print(char_min, char_max)
    line_max = len(words) # Max "Height"
    line_min = 1          # Min "Height"
#     print(line_min, line_max)
    word_max = max(map(len,words))  # Max "Word"
    word_min = min(map(len,words))  # Min "Word"
#     print(word_min, word_max)
    sets = {}
#     print(line_min,line_max)
#     print(word_min,word_max)
    centroid = lambda number: product([(i,number//i) for i in range(1,number//2+1) if number//i == number/i and i<number/i][-1])
#     print(centroid(len("".join(words))))
#     print(centroid(len(" ".join(words))))
#     centroid = centroid(char_max)
    for factor in range(1, len(words)+1):
        lines   = []              
        length  = char_max/factor
#         print(factor, length)
        line    = []
        for word in words :
#             if sum(map(len,line)) + len(word) + len(line) <= length :
#                 line  += word
#             print(line, sum(map(len, line)), word, len(word), length)
            if sum(map(len, line)) + len(word) <= length:
                line.append(word)
            else :    
                lines.append(line)
                line = [word]
#                 line = [word]
        if line : lines.append(line)
        centroid = metric([len(" ".join(line))for line in lines])
        sets[max([len(" ".join(line)) for line in lines])**2 + len(lines)**2] = lines # [(sum(map(len," ".join(line))), lines) for line in lines]
#         sets["{1} ({0})".format(factor, max([(len(" ".join(line))) for line in lines])**2 + len(lines)**2)] = lines # [(sum(map(len," ".join(line))), lines) for line in lines]
#     pprint(sets)
#     pprint(sets[min(sets)])
    return sets[min(sets)]

#     for factor in range(1,word_max):
#         tail = 0
#         step = words/factor
#         factors = []             # e.g. 3 words per line 
#         length  = line_max//step # e.g. 8 chars per line
#         for head in range(step:words:step) :
#             factors.append(sum(words[tail:head])) # Use a more fluid packing here
#             tail = head
#         sets[factor] = max(factors)

if __name__ == "__main__" :

    paragraph("A B".split(" "))
    paragraph("A B C".split(" "))
    paragraph("A B C D".split(" "))
    
    # paragraph("Self Help".split(" "))
    # paragraph("There are three".split(" "))
    # paragraph("There stage three".split(" "))
    
    paragraph("AA B C".split(" "))
    paragraph("A BB C".split(" "))
    paragraph("A B CC".split(" "))
