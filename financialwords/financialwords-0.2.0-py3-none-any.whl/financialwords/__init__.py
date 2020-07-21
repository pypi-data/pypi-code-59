import os

module_path = os.path.dirname(__file__)
def _read_financialwords():
    financialwords = set()
    with open(os.path.join(module_path, 'words.txt')) as f:
        for line in f:
            financialwords.add(line[:-1])
    return financialwords

def filter(input_list):
    return [i for i in input_list if i not in financialwords]

financialwords = _read_financialwords()