'''
Fichier contenant des algorythmes utilitaires.
'''

import re
from typing import List, Tuple

from src.classes.const_regex import REGEX_INLINE, REGEX_MULTILIGNE

#typer en sortie ?
def recup_client(id_: str):
    '''
    description
    '''
    from .parser import Parser
    tmp = re.split('\\.', id_)
    return Parser.list_clients[int(tmp[0]) - 1]

def recup_script(id_: str):
    '''
    description
    '''
    from .parser import Parser
    tmp = re.split('\\.', id_)
    return Parser.list_clients[int(tmp[0]) - 1].list_scripts[int(tmp[1]) - 1]


def nb_lignes(multiligne: str) -> int:
    '''
    description
    '''
    return len(re.split('[\n\r]', multiligne))


def extraction_inligne(ligne: str) -> Tuple[str, str]:
    '''
    description
    '''
    tmp = re.split(REGEX_INLINE, ligne)
    return tmp[0] + '\n', tmp[1]


def extraction_multiligne(text: str) -> Tuple[str, List[str]]:
    '''
    description
    '''
    ligne = ""
    comment = []
    pattern = re.compile(REGEX_MULTILIGNE)
    tmp = re.split(REGEX_MULTILIGNE, text)

    i = 0
    while i < len(tmp):
        if pattern.match(tmp[i]):
            comment.append(tmp[i])
            if nb_lignes(tmp[i]) > 1:
                ligne += '\n'
            if i < (len(tmp) - 1):
                i += 1
        else:
            ligne += tmp[i]
        i += 1
    return ligne, comment
    