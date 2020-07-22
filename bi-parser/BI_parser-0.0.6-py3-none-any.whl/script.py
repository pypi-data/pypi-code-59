'''
Contient la classe chargée de traiter, stocker et manipuler les informations liées aux scripts.
'''

import re
from typing import List

import xlsxwriter

from BI_parser.bloc import Bloc
from BI_parser.requete import Requete
from BI_parser.commentaire import Commentaire

from BI_parser.const_regex import REGEX_LIGNE_VIDE, REGEX_TOUT, REGEX_MULTILIGNE, REGEX_INLINE
from BI_parser.utils import extraction_inligne, extraction_multiligne, nb_lignes


class Script:
    '''
    description
    '''

    def __init__(self, chemin_du_script: str, id_: str) -> None:
        '''
        description
        '''

        self.nom: str = chemin_du_script.split('/')[-1]
        self.id: str = id_
        self.langage: str = self.nom.split('.')[-1]
        self.type: str = '3'
        self.chemin: str = chemin_du_script
        self.description: str = "3"

        self.list_blocs: List[Bloc] = []

        self.contenu: List[str] = open(chemin_du_script).readlines()
        self.list_blocs: List[Bloc] = create_blocs(self, self.contenu)

        self.workbook = self._get_excel_base()
        self.cpt_excel = 3

    def nb_blocs(self) -> int:
        '''
        description
        '''

        return len(self.list_blocs)

    def nb_requetes(self) -> int:
        '''
        description
        '''

        acc = 0
        for bloc in self.list_blocs:
            if isinstance(bloc, Requete):
                acc += 1
        return acc

    def nb_commentaires(self) -> int:
        '''
        description
        '''
        acc = 0
        for bloc in self.list_blocs:
            if isinstance(bloc, Commentaire):
                acc += 1
        return acc

    def nb_commentaires_structure(self) -> int:
        '''
        description
        '''
        acc = 0
        for bloc in self.list_blocs:
            if isinstance(bloc, Commentaire):
                if not bloc.explicatif:
                    acc += 1
        return acc

    def nb_commentaires_explicatif(self) -> int:
        '''
        description
        '''
        acc = 0
        for bloc in self.list_blocs:
            if isinstance(bloc, Commentaire):
                if bloc.explicatif:
                    acc += 1
        return acc


    def nb_lignes_commentaire(self) -> int:
        '''
        description
        '''
        acc = 0
        for bloc in self.list_blocs:
            if isinstance(bloc, Commentaire):
                if bloc.explicatif:
                    acc += bloc.nb_lignes()
        return acc

    def nb_lignes_requete(self) -> int:
        '''
        description
        '''
        acc = 0
        for bloc in self.list_blocs:
            if isinstance(bloc, Requete):
                acc += bloc.nb_lignes()
        return acc

    def nb_lignes(self) -> int:
        '''
        description
        '''
        return len(self.contenu)

    def nb_caracteres(self) -> int:
        '''
        description
        '''
        acc = 0
        for (_, ligne) in enumerate(self.contenu):
            acc += len(ligne)
        return acc

    def nb_caracteres_requete(self) -> int:
        '''
        description
        '''
        acc = 0
        for bloc in self.list_blocs:
            if isinstance(bloc, Requete):
                acc += bloc.nb_caracteres()
        return acc

    def nb_caracteres_commentaire(self) -> int:
        '''
        description
        '''
        acc = 0
        for bloc in self.list_blocs:
            if isinstance(bloc, Commentaire):
                if bloc.explicatif:
                    acc += bloc.nb_caracteres()
        return acc

    def script_to_excel(self) -> None:
        '''
        description
        '''

        cpt_select = 0

        for bloc in self.list_blocs:
            if isinstance(bloc, Requete):
                if bool(re.search('^([\t \n\r]*SELECT )', bloc.request)):
                    cpt_select += 1
                self.workbook = bloc.query_to_excel(self.workbook, cpt_select)

        # Pour le contour du tableau
        border_table_right_format = self.workbook.add_format({'left': 5})
        border_table_bot_format = self.workbook.add_format({'top': 5})

        worksheet = self.workbook.get_worksheet_by_name("tableau")

        for i in range(1, self.cpt_excel):
            worksheet.write('H' + str(i), '', border_table_right_format)

        for i in range(ord('H') - 65):
            worksheet.write(str(chr(i + 65)) + str(self.cpt_excel), '', border_table_bot_format)

        self.workbook.close()

    def _get_excel_base(self) -> xlsxwriter.Workbook:
        """
        Retourne un squelette à remplir pour la restitution sous forme de tableau Excel
        param : workbook : fichier Excel
        return : workbook : le squelette Excel
        """
        workbook = xlsxwriter.Workbook('cartographie.xlsx')

        worksheet = workbook.add_worksheet("tableau")

        merge_format = workbook.add_format({
            'bold': 1,
            'border': 5,
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': '#B5C5E0'})
        worksheet.set_column('A:G', 20)

        title_format = workbook.add_format({
            'align': 'center',
            'border': 1,
            'valign': 'vcenter',
            'fg_color': '#CED4DF'})

        title_cle_format = workbook.add_format({
            'align': 'center',
            'border': 1,
            'valign': 'vcenter',
            'fg_color': '#CED4DF',
            'right': 5})

        title_type_format = workbook.add_format({
            'align': 'center',
            'border': 1,
            'valign': 'vcenter',
            'fg_color': '#CED4DF',
            'left': 5})

        worksheet.merge_range('A1:B1', 'Source', merge_format)
        worksheet.merge_range('C1:E1', 'Lien', merge_format)
        worksheet.merge_range('F1:G1', 'Cible', merge_format)

        worksheet.write('A2', 'Système', title_format)
        worksheet.write('B2', 'Table', title_format)
        worksheet.write('C2', 'Type de lien', title_type_format)
        worksheet.write('D2', 'Propriété du script', title_format)
        worksheet.write('E2', 'Clé de jointure', title_cle_format)
        worksheet.write('F2', 'Système', title_format)
        worksheet.write('G2', 'Table', title_format)

        return workbook


def create_blocs(script: Script, texte: List[str]) -> List[Bloc]:
    '''
    Segmente texte et renvoie une liste des Blocs initialisés.
    '''

    list_blocs: List[Bloc] = []

    pattern_ligne_vide = re.compile(REGEX_LIGNE_VIDE)
    pattern_commentaire_inligne = re.compile(REGEX_TOUT + REGEX_INLINE)
    pattern_commentaire_multiligne = re.compile(REGEX_TOUT + REGEX_MULTILIGNE)
    pattern_fin_de_requete = re.compile(REGEX_TOUT + ';' + REGEX_TOUT)

    debut_statement = 1
    ligne_ag: str = ""

    for (i, ligne) in enumerate(texte, 1):

        if pattern_commentaire_inligne.match(ligne):
            # separe le commentaire du reste de la ligne et créé une instance de commentaire
            (ligne, ext_comment) = extraction_inligne(ligne)
            list_blocs.append(Commentaire(ext_comment, i, i, script.id + '.' + str(len(list_blocs) + 1)))

        ligne_ag += ligne

        if pattern_commentaire_multiligne.match(ligne_ag):
            (ligne_ag, ext_comment) = extraction_multiligne(ligne_ag)
            for j in ext_comment:
                list_blocs.append(Commentaire(j, (i - nb_lignes(j)) + 1, i, script.id + '.' + str(len(list_blocs) + 1)))

        if pattern_ligne_vide.match(ligne_ag):
            # pour l'instant on ne stocke pas les ligne vide
            ligne_ag = ""
            debut_statement = i + 1

        if pattern_fin_de_requete.match(ligne_ag):
            # stocker ou creer instance de requete
            list_blocs.append(Requete(ligne_ag, debut_statement, i, script.id + '.' + str(len(list_blocs) + 1)))
            ligne_ag = ""
            debut_statement = i + 1

    return list_blocs
