
from .script import Script
from .bloc import Bloc

class Commentaire(Bloc):
    '''
    description
    '''

    def __init__(self, pere: Script, texte: str, debut: int, fin: int, id_: str) -> None:
        '''
        description
        '''

        Bloc.__init__(self, pere, texte, debut, fin, id_)
