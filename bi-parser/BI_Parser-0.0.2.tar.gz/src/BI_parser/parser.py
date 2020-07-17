
from typing import List

from .client import Client


class Parser:
    '''
    description
    '''

    def __init__(self) -> None:  # Notre méthode constructeur
        '''
        description
        '''

        self.list_clients: List[Client] = []

    def parse(self, chemin_du_repertoire: str, nom_du_client: str = '', langage: str = 'sql') -> None:
        '''
        description
        '''

        self.list_clients.append(Client(self, chemin_du_repertoire, str(len(self.list_clients) + 1), nom_du_client, langage))

    def _get_list_clients(self):
        return self.list_clients
