
from abc import abstractmethod
from typing import List

from .script import Script
from .bloc import Bloc
from .variable import Variable

class Code(Bloc):
    '''
    description
    '''

    @abstractmethod
    def __init__(self, pere: Script, texte: str, debut: int, fin: int, id_: str) -> None:
        '''
        description
        '''

        Bloc.__init__(self, pere, texte, debut, fin, id_)
        self.var_utilise: List[Variable] = []
        self.var_declare: List[Variable] = []

    def imbrication_max(self) -> int:
        '''
        description
        '''

        # à renseigner
        return 6  # temporaire

    def imbrication_nb(self) -> int:
        '''
        description
        '''

        # à renseigner
        return 6  # temporaire

    def imbrication_moyenne(self) -> int:
        '''
        description
        '''

        # à renseigner
        return 6  # temporaire
