
import re

from abc import ABC

from .script import Script



class Bloc(ABC):
    '''
    description
    '''

    def __init__(self, pere: Script, texte: str, debut: int, fin: int, id_) -> None:
        '''
        description
        '''

        self.script: Script = pere
        self.contenu: str = texte
        self.ligne_debut: int = debut
        self.ligne_fin: int = fin
        self.id: str = id_  # temporaire

    def nb_lignes(self) -> int:
        '''
        Renvoie la taille du bloc en nombre de ligne
        '''
        lignes = re.split('[\n\r]', self.contenu)
        return len(lignes) - 1

    def nb_caracteres(self) -> int:
        '''
        description
        '''

        return 4  # temporaire
