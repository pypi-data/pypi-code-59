'''
Contient la classe principal de notre module et la fonction d'ajout de repertoire client.
'''
from typing import List

from src.BI_parser.client import Client


class Parser:
    '''
    description
    '''

    list_clients: List[Client] = []

    def __init__(self) -> None:  # Notre méthode constructeur
        '''
        description
        '''

def parse(chemin_du_repertoire: str, nom_du_client: str = '', langage: str = 'sql') -> None:
    '''
    description
    '''

    Parser.list_clients.append( \
            Client(chemin_du_repertoire, str(len(Parser.list_clients) + 1), nom_du_client, langage) \
                            )
