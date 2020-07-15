from typing import List
from abc import ABC, abstractmethod


class Parser:

    def __init__(self) -> None:  # Notre méthode constructeur

        self.list_clients: List[Client] = []

    def parse(self, chemin_du_repertoire: str) -> None:

        self.list_clients.append(Client(self, chemin_du_repertoire))

    def _get_list_clients(self):
        return self.list_clients


class Client:

    def __init__(self, pere: Parser, chemin_du_repertoire: str) -> None:
        # lancer les constructeurs des scripts
        self.list_scripts: List[Script] = []
        self.parser: Parser = pere
        self.nom: str = '2'  # implementation de Julien
        self.id: str = '2'  # implementation de Julien
        self.langage: str = 'sql'  # implémentation de Julien

    def nb_scripts(self) -> int:
        return len(self.list_scripts)

    def nb_blocs(self) -> int:
        acc = 0
        for i in self.list_scripts:
            acc += i.nb_blocs()
        return acc

    def nb_requetes(self) -> int:
        acc = 0
        for i in self.list_scripts:
            acc += i.nb_requetes()
        return acc

    def nb_commentaires(self) -> int:
        acc = 0
        for i in self.list_scripts:
            acc += i.nb_commentaires()
        return acc

    def nb_lignes(self) -> int:
        acc = 0
        for i in self.list_scripts:
            acc += i.nb_lignes()
        return acc

    def nb_caracteres(self) -> int:
        acc = 0
        for i in self.list_scripts:
            acc += i.nb_caracteres()
        return acc


class Script:

    def __init__(self, pere: Client, contenu: str) -> None:
        # segmenter contenue en bloc
        # for each bloc appeler constructeur
        # lancer les constructeurs des blocs
        self.list_blocs: List[Bloc] = []
        self.client: Client = pere
        self.nom: str = '3'  # temporaire
        self.id: str = '3'  # temporaire
        self.type: str = '3'  # temporaire
        self.description: str = "3"  # temporaire

    def nb_blocs(self) -> int:
        return len(self.list_blocs)

    def nb_requetes(self) -> int:
        acc = 0
        for i in self.list_blocs:
            if isinstance(i, Requete):
                acc += 1
        return acc

    def nb_commentaires(self) -> int:
        acc = 0
        for i in self.list_blocs:
            if isinstance(i, Commentaire):
                acc += 1
        return acc

    def nb_lignes(self) -> int:
        acc = 0
        for i in self.list_blocs:
            acc += i.nb_lignes()
        return acc

    def nb_caracteres(self) -> int:
        acc = 0
        for i in self.list_blocs:
            acc += i.nb_caracteres()
        return acc


# à besoin de la bibliotheque abc
class Bloc(ABC):

    def __init__(self, pere: Script, texte: str) -> None:
        self.contenue: str = texte
        self.id: str = '4'  # temporaire
        self.ligne_debut: int = 4  # temporaire
        self.ligne_fin: int = 4  # temporaire
        self.script: Script = pere

    def nb_commentaires(self) -> int:
        return 4  # temporaire

    def nb_lignes(self) -> int:
        return 4  # temporaire

    def nb_caracteres(self) -> int:
        return 4  # temporaire


class Commentaire(Bloc):
    def __init__(self, pere: Script, texte: str) -> None:
        Bloc.__init__(self, pere, texte)


class Code(Bloc):
    @abstractmethod
    def __init__(self, pere: Script, texte: str) -> None:
        Bloc.__init__(self, pere, texte)
        self.var_utilise: List[Variable] = []
        self.var_declare: List[Variable] = []

    def imbrication_max(self) -> int:
        # à renseigner
        return 6  # temporaire

    def imbrication_nb(self) -> int:
        # à renseigner
        return 6  # temporaire

    def imbrication_moyenne(self) -> int:
        # à renseigner
        return 6  # temporaire


class Requete(Code):
    def __init__(self, pere: Script, texte: str) -> None:
        Code.__init__(self, pere, texte)


class Variable(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass


class Table(Variable):
    def __init__(self, val: int) -> None:  # int est temporaire
        Variable.__init__(self)
        self.valeur = val
