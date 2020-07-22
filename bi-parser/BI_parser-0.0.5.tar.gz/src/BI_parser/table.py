'''
Contient la classe chargée de traiter, stocker et manipuler les informations liées aux tables.
'''

from src.BI_parser.variable import Variable


class Table(Variable):
    '''
    description
    '''

    def __init__(self, nom: str = "", alias: str = "", type_table: str = "") -> None:
        Variable.__init__(self)
        self.nom = nom
        self.alias = alias
        self.type_table = type_table
