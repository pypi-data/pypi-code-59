import os
import re
import xlsxwriter
from typing import List, Tuple
from abc import ABC
import sqlparse

from abc import abstractmethod
from sqlparse.tokens import Wildcard, Keyword, Punctuation, DDL, DML, Name, Literal
from sqlparse.sql import TokenList, Identifier, IdentifierList, Function, Operation, Parenthesis, Where


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


class Client:
    '''
    description
    '''

    def __init__(self, pere: Parser, chemin_du_repertoire: str, id_: str, nom_du_client: str, langage: str) -> None:
        '''
        description
        '''
        self.parser: Parser = pere
        self.nom: str = nom_du_client  # temporairement déclaratif
        self.id: str = id_
        self.langage: str = langage  # temporairement déclaratif

        self.list_scripts: List[Script] = []
        list_chemin_scripts: List[str] = os.listdir(chemin_du_repertoire)
        for chemin in list_chemin_scripts:
            self.list_scripts.append(Script(self, chemin_du_repertoire + '/' + chemin, self.id + '.' + str(len(self.list_scripts) + 1)))

    def nb_scripts(self) -> int:
        '''
        description
        '''

        return len(self.list_scripts)

    def nb_blocs(self) -> int:
        '''
        description
        '''

        acc = 0
        for script in self.list_scripts:
            acc += script.nb_blocs()
        return acc

    def nb_requetes(self) -> int:
        '''
        description
        '''

        acc = 0
        for script in self.list_scripts:
            acc += script.nb_requetes()
        return acc

    def nb_commentaires(self) -> int:
        '''
        description
        '''

        acc = 0
        for script in self.list_scripts:
            acc += script.nb_commentaires()
        return acc

    def nb_lignes(self) -> int:
        '''
        description
        '''

        acc = 0
        for script in self.list_scripts:
            acc += script.nb_lignes()
        return acc

    def nb_caracteres(self) -> int:
        '''
        description
        '''

        acc = 0
        for script in self.list_scripts:
            acc += script.nb_caracteres()
        return acc


class Script:
    '''
    description
    '''

    def __init__(self, pere: Client, chemin_du_script: str, id_: str) -> None:
        '''
        description
        '''
        self.client: Client = pere
        self.nom: str = chemin_du_script.split('/')[-1]  # temporaire
        self.id: str = id_  # temporaire
        self.langage: str = self.nom.split('.')[-1]  # temporaire
        self.type: str = '3'  # temporaire
        self.description: str = "3"  # temporaire

        self.list_blocs : List[Bloc] = []

        self.contenu: List[str] = open(chemin_du_script).readlines()
        self.list_blocs = create_blocs(self, self.contenu)

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
        return len(self.contenu)

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
        for bloc in self.list_blocs:
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


class Requete(Code):
    '''
    description
    '''

    def __init__(self, pere: Script, texte: str, debut: int, fin: int, id_: str) -> None:
        Code.__init__(self, pere, texte, debut, fin, id_)
        self.dict_infos = {'Variables': [], 'Functions': [], 'Var_raw': [], 'Var_def': [],
                           'list_comparaisons': [],
                           'list_references': [], 'cpt_join': 0, 'type': None}
        self.request = sqlparse.format(texte, keyword_case='upper', strip_comments=True, strip_whitespace=True)
        self.script = pere
        self.type = None
        self._detect_type_query(sqlparse.parse(self.request)[0])

    def _fetch_from_select(self, query: TokenList, flag: int = False, flag_from: int = False,
                           flag_where: int = False) -> None:
        """
        Traitement des SELECT
        :param: query: Le code à analyser
        :param: flag: booléen utilisé pour détecter les tables
        """
        join = None

        for token in query:
            # Les espaces ne sont pas traités
            if token.is_whitespace:
                continue

            # Ajout des tables
            if flag and isinstance(token, Identifier) and token.value[0] != '(':
                if flag_from:
                    self.var_utilise.append(new_table(token.value, 'Tables_from'))
                else:
                    self.var_utilise.append(new_table(token.value, 'Tables'))
                continue
            elif flag and isinstance(token, Identifier) and token.value[0] == '(':
                self.var_utilise.append(new_table(token.value, 'Tmp_Tables'))
                self._fetch_from_select(token[0], True, flag_from, flag_where)
                continue
            elif flag and isinstance(token, IdentifierList):
                self._fetch_from_select(token, True, flag_from, flag_where)
                continue
            elif token.value != ",":
                flag = False
                flag_from = False

            if token.value == "HAVING":
                flag_where = True

            if isinstance(token, Function):
                self._fetch_from_select(token[1])
                continue
            elif isinstance(token, Parenthesis):
                self._fetch_from_select(token)
                continue
            elif isinstance(token, Operation) and token.value[0] == '(':
                self.var_utilise.append(new_table(token.value, 'Tmp_Tables'))
                self._fetch_from_select(token)
                continue
            elif isinstance(token, Identifier) and token.value[0] == '(':
                self.var_utilise.append(new_table(token.value, 'Tmp_Tables'))
                self._fetch_from_select(token[0])
                continue

            # Ajout des variables
            if not flag and isinstance(token, Identifier):
                self.dict_infos['Variables'].append(token.value)
                continue
            elif not flag and isinstance(token, IdentifierList):
                self._fetch_from_select(token)
                continue
            elif not flag_where and isinstance(token, sqlparse.sql.Comparison):
                self.dict_infos['list_comparaisons'].append(
                    join + "##" + str(self.dict_infos['cpt_join']) + "##" + token.value)
                self._fetch_from_select(token)
                continue
            elif isinstance(token, Where):
                self._fetch_from_select(token, flag_where=True)
                continue
            elif isinstance(token, sqlparse.sql.Token) and token.ttype == Wildcard:
                self.dict_infos['Variables'].append(token.value)

            if not isinstance(token, TokenList):
                if token.ttype == Keyword and (token.value == 'FROM' or "JOIN" in token.value):
                    flag = True
                    self.dict_infos['cpt_join'] += 1
                    if token.value == 'FROM':
                        flag_from = True
                    else:
                        join = token.value

    def _fetch_from_ddl(self, query: TokenList) -> None:
        """
        Traitement des CREATE TABLE
        :param: query: Le code à analyser
        """
        # booléen utilisé pour détecter les clés étrangères
        flag = False
        reference = ""
        for token in query:
            if token.value == "REFERENCES":
                flag = True
                reference += self.dict_infos['Variables'][-1] + "##"

            if token.is_whitespace or token.ttype in [DML, Keyword, Punctuation]:
                continue

            if bool(re.search('KEY\\(' + REG_w + '+\\)', token.value)):
                self.dict_infos['Variables'].append(re.search(r'KEY\((.*)\)', token.value.replace("\"", "")).group(1))
            elif not flag and isinstance(token, Identifier):
                self.dict_infos['Variables'].append(token.value.replace("\"", ""))
            elif flag and (isinstance(token, Identifier) or isinstance(token, Function)):
                self.var_utilise.append(new_table(token.value, 'Tables'))
                flag = False
                reference += token.value
                self.dict_infos['list_references'].append(reference)
                reference = ""
            elif isinstance(token, Parenthesis) or isinstance(token, IdentifierList):
                self._fetch_from_ddl(token)

    def _fetch_from_update(self, query: TokenList, flag: int = False, query_select: TokenList = None) -> None:
        """
        Traitement des UPDATE
        :param: query: Le code à analyser
        """

        for token in query:
            if token.is_whitespace or token.ttype == Punctuation:
                continue
            elif query_select is not None and token.ttype == DML and token.value == "SELECT":
                self._fetch_from_select(query_select)
                return
            elif (token.ttype == Keyword or token.ttype == DML) and (
                    token.value in ['FROM', 'UPDATE'] or "JOIN" in token.value):
                flag = True
            elif token.ttype == Keyword:
                flag = False

            if flag and isinstance(token, Identifier):
                self.var_utilise.append(new_table(token.value, 'Tables'))
            elif not flag and isinstance(token, Identifier):
                self.dict_infos['Variables'].append(token.value.replace("\"", ""))
            elif isinstance(token, IdentifierList) or isinstance(token, Where) or isinstance(token,
                                                                                             sqlparse.sql.Comparison):
                self._fetch_from_update(token, flag)
            elif isinstance(token, Parenthesis):
                self._fetch_from_update(query=token, query_select=token)

    def _fetch_from_insert(self, query: TokenList, flag: int = False, flag_insert: int = False) -> None:
        """
        Traitement des INSERT
        :param: query: Le code à analyser
        :param: flag: booléen utilisé pour détecter les variables
        :param: flag_insert: booléen pour ne pas prendre en compte les fonctions TOP (w/o PERCENT), etc.
        """
        i = 0

        for token in query:
            i += 1
            if token.value == "INTO":
                flag_insert = True
            if token.is_whitespace or not flag_insert:
                continue

            if isinstance(token, Identifier):
                self.var_utilise.append(new_table(token.value, 'Tables'))
            elif isinstance(token, Function) or isinstance(token, Parenthesis):
                self._fetch_from_insert(token, True, True)
            elif flag and isinstance(token, TokenList):
                self.dict_infos['Variables'].append(token.value.replace("\"", ""))
            elif token.ttype == DML and token.value == "SELECT":
                self._fetch_from_select(query[i:])
                return

    def _fetch_from_function(self, query: TokenList) -> None:
        """
        Analyse les fonctions.
        :param: query: Le code à analyser
        """
        for token in query:
            if token.is_whitespace:
                continue

            if isinstance(token, TokenList):
                self._fetch_from_function(token)
            elif isinstance(token, sqlparse.sql.Token) and token.value[0] == '$':
                if bool(re.search('[^' + REG_S + ']BEGIN', token.value)) \
                and bool(re.search('[^' + REG_S + ']END;', token.value)):
                    qparse = sqlparse.split(re.search('[^' + REG_S + ']BEGIN(.*)END;', \
                                                        re.sub(REG_s, ' ', token.value) \
                                                        ).group(1))
                else:
                    qparse = sqlparse.split(re.search('\\$\\$(.*)\\$\\$', \
                                                        re.sub(REG_s, ' ', token.value) \
                                                        ).group(1))

                for q in qparse:
                    self._detect_type_query(sqlparse.parse(q)[0])

    def _detect_type_query(self, query: TokenList) -> None:
        """
        Détecte le type de commande SQL utilisé pour appeler les fonctions correspondantes
        :param: query: Le code à analyser
        """
        i = 0

        while query.tokens[i].is_whitespace or query.tokens[i] is None:
            i += 1

        query_type = query.tokens[0].ttype
        self.type = query.tokens[i].value

        if query_type == DML:

            if self.type == "SELECT":
                self._fetch_from_select(query)
            elif self.type == "INSERT":
                self._fetch_from_insert(query)
            elif self.type == "UPDATE":
                self._fetch_from_update(query)

        if query_type == DDL or self.type == 'TRUNCATE':
            flag = False
            flag_table = False

            if query.tokens[2].value == "FUNCTION":
                self.dict_infos['Functions'].append(query.tokens[4].tokens[0].value)

                for t in query.tokens[4].tokens[1]:
                    if isinstance(t, Identifier):
                        self.dict_infos['Var_def'].append(t.value)

                if bool(re.search('[^' + REG_S + ']DECLARE', query.value)):
                    qparse = sqlparse.split(re.search('DECLARE(.*)BEGIN', \
                                            re.sub(REG_s, ' ', query.value) \
                                            ).group(1))
                    for q in qparse:
                        if bool(re.search( \
                                            '=' + REG_s + '*(' + REG_d + '+[\\.]?' + REG_d + \
                                            '*|[\'\"].+[\'\"])(' + REG_s + '*;' + REG_s + '*)$' \
                                            , q)):
                            self.dict_infos['Var_raw'].append(q.split(" ")[0])
                        else:
                            self.dict_infos['Var_def'].append(q.split(" ")[0])
                self._fetch_from_function(query)
                return

            for token in query.tokens:

                if token.is_whitespace or token.ttype in [DDL, Keyword, Punctuation]:
                    continue

                if isinstance(token, Parenthesis):
                    if bool(re.search('^(' + REG_s + '*\\(' + REG_s + '*SELECT )', token.value)):
                        self._fetch_from_select(token)
                    else:
                        self._fetch_from_ddl(token)
                elif "CREATE" in self.type:
                    if query.tokens[2].value == "TABLE" or query.tokens[4].value == "TABLE":
                        if token.value == "SELECT":
                            q = "SELECT " + re.search('SELECT(.*)\\;', query.value).group(1) + ";"
                            self._fetch_from_select(sqlparse.parse(q)[0])
                            return

                        for t in token.tokens:
                            if t.is_whitespace or t.ttype == Punctuation:
                                continue

                            if t.ttype in [Name, Literal.String.Symbol]:
                                self.var_utilise.append(new_table(token.value, 'New_Tables'))
                            elif t.value == "AS":
                                flag = True
                            elif not flag:
                                self._fetch_from_ddl(t)
                            else:
                                self._fetch_from_select(t)
                                flag = False
                elif self.type == "ALTER":
                    for t in token:
                        if t.ttype == Name and not flag_table:
                            self.var_utilise.append(new_table(token.value, 'Tables'))
                            flag_table = True
                        elif t.ttype == Name:
                            self.dict_infos['Variables'].append(t.value.replace("\"", ""))
                elif self.type in ["DROP", "TRUNCATE"]:
                    if isinstance(token, Identifier):
                        self.var_utilise.append(new_table(token.value, 'Tables'))

    def _get_tables(self) -> List[str]:
        """"
        Retourne toutes les tables récupérées
        :return : Une liste des tables uniques
        """
        return list(set([var.nom for var in self.var_utilise if isinstance(var, Table)]))

    def query_to_excel(self, workbook: xlsxwriter.Workbook, num_select: int = 1) -> xlsxwriter.Workbook:
        """
        Remplit le fichier Excel en entrée avec les valeurs de cette requete
        :param workbook: Le fichier Excel
        :param num_select: Le nombre de commande de type SELECT dans le fichier Excel
        :return: le fichier Excel rempli
        """
        cpt = self.script.cpt_excel
        source = 'B'
        cible = 'G'
        type_lien = 'C'
        cle = 'E'
        cible_cell = ''
        list_comparaison_join = []

        cell_format = workbook.add_format({
            'align': 'center',
            'valign': 'vcenter',
            'text_wrap': True})

        cell_cle_format = workbook.add_format({
            'align': 'center',
            'valign': 'vcenter',
            'text_wrap': True,
            'right': 5})
        cell_type_format = workbook.add_format({
            'align': 'center',
            'valign': 'vcenter',
            'text_wrap': True,
            'left': 5})

        #list_from = [x.alias for x in self.var_utilise if isinstance(x, Table) and x.type_table == "Tables_from"]

        list_join = [x.alias for x in self.var_utilise if isinstance(x, Table) and x.type_table == "Tables"]
        dict_table = {x.nom: [] for x in self.var_utilise if isinstance(x, Table) and
                      x.type_table in ["Tables", "Tables_from"]}

        for x in [x for x in self.var_utilise if isinstance(x, Table) and x.type_table in ["Tables", "Tables_from"]]:
            dict_table[x.nom].append(x.alias)

        worksheet = workbook.get_worksheet_by_name("tableau")

        if self.type == 'SELECT':
            cible_cell = "VUE TEMPORAIRE " + str(num_select)

        elif bool(re.search( \
                            '^(' + REG_s + '*CREATE' + REG_s + '*(OR)?' + REG_s + '*(REPLACE)?' + REG_s + '*TABLE)' \
                            , self.request)) \
                or \
                bool(re.search('^(' + REG_s + '*CREATE' + REG_s + '*TEMPORARY' + REG_s + '*TABLE)', self.request)):

            if not bool(re.search('^(' + REG_s + '*CREATE' + REG_s + '*TEMPORARY' + REG_s + '*TABLE)', self.request)):
                cible_cell = [x.nom for x in self.var_utilise if isinstance(x, Table) and x.type_table == "New_Tables"][0]
            else:
                cible_cell = "TABLE " + \
                             [x.nom for x in self.var_utilise if isinstance(x, Table) and x.type_table == "New_Tables"][0] + \
                             " TEMPORAIRE"

            worksheet.write(type_lien + str(cpt), "CREATE", cell_type_format)
            worksheet.write(cle + str(cpt), "", cell_cle_format)
            worksheet.write(cible + str(cpt), cible_cell, cell_format)
            cpt += 1

            for r in self.dict_infos['list_references']:
                left, right = r.split('##')
                table = right.split("(")[0]
                worksheet.write(cible + str(cpt), cible_cell, cell_format)
                worksheet.write(type_lien + str(cpt), "REFERENCE", cell_type_format)
                worksheet.write(source + str(cpt), table, cell_format)

                if bool(re.search(REG_w + '+\\(' + REG_w + '+\\)', right)):
                    cle_left = re.search('\\((.*)\\)', right).group(1)
                    worksheet.write(cle + str(cpt), table + "." + cle_left + "=" + cible_cell + "." + left,
                                    cell_cle_format)
                else:
                    worksheet.write(cle + str(cpt), left, cell_cle_format)
                cpt += 1

        for t in [x for x in self.var_utilise if isinstance(x, Table) and x.type_table == "Tables_from"]:
            worksheet.write(type_lien + str(cpt), "FROM", cell_type_format)
            worksheet.write(source + str(cpt), t.nom, cell_format)
            worksheet.write(cle + str(cpt), "", cell_cle_format)
            worksheet.write(cible + str(cpt), cible_cell, cell_format)

            cpt += 1

        if len(self.dict_infos['list_comparaisons']) > 0:
            # Les numéros attribués ne commencent pas forcément à 0
            _, min_index, _ = self.dict_infos['list_comparaisons'][0].split('##')

            for _, comp in enumerate(self.dict_infos['list_comparaisons']):
                if bool(re.search('=' + REG_s + '*(' + REG_d + '+[\\.]?' + REG_d + '*|[\'\"].+[\'\"])', comp)):
                    continue

                join, num, comp = comp.split("##")
                num = int(num) - int(min_index)

                if len(list_comparaison_join) <= num:
                    list_comparaison_join.append([])
                    list_comparaison_join[num].append(join)
                    list_comparaison_join[num].append(comp)
                else:
                    list_comparaison_join[num].append(comp)

            for comp in list_comparaison_join:
                join = comp[0]
                table = None

                for c in comp[1:]:
                    left, right = c.replace(" ", "").split("=")

                    left_param = left.split(".")[0]
                    right_param = right.split(".")[0]
                    if left_param in list_join:
                        table = left_param
                        list_join.remove(left_param)
                    elif right_param in list_join:
                        table = right_param
                        list_join.remove(right_param)

                origin_table = [k for k, l in dict_table.items() if table in l][0]

                if not origin_table == table:
                    table = origin_table + ' ' + table

                worksheet.write(cible + str(cpt), cible_cell, cell_format)

                worksheet.write(type_lien + str(cpt), join, cell_type_format)
                worksheet.write(cle + str(cpt), " AND ".join(comp[1:]), cell_cle_format)
                worksheet.write(source + str(cpt), table, cell_format)
                cpt += 1

        self.script.cpt_excel = cpt

        return workbook



class Commentaire(Bloc):
    '''
    description
    '''

    def __init__(self, pere: Script, texte: str, debut: int, fin: int, id_: str) -> None:
        '''
        description
        '''

        Bloc.__init__(self, pere, texte, debut, fin, id_)



class Commentaire(Bloc):
    '''
    description
    '''

    def __init__(self, pere: Script, texte: str, debut: int, fin: int, id_: str) -> None:
        '''
        description
        '''

        Bloc.__init__(self, pere, texte, debut, fin, id_)




class Variable(ABC):
    '''
    description
    '''

    @abstractmethod
    def __init__(self) -> None:
        pass

class Table(Variable):
    '''
    description
    '''

    def __init__(self, nom: str = "", alias: str = "", type_table: str = "") -> None:
        Variable.__init__(self)
        self.nom = nom
        self.alias = alias
        self.type_table = type_table


# Constantes RegEx

REG_s = '[ \t\n\r\f\v]'
REG_S = '[^ \t\n\r\f\v]'
REG_d = '[0-9]'
REG_D = '[^0-9]'
REG_w = '[a-zA-Z0-9_]'
REG_W = '[^a-zA-Z0-9_]'

REGEX_MULTILIGNE = '(' + '/\\*' + '(.|[\r\n])*?' + '\\*/' + ')'
REGEX_INLINE = '(' + '--.*' + '|' + '#.*' + ')'
REGEX_LIGNE_VIDE = '^' + REG_s + '*$'
REGEX_TOUT = '(.|[\r\n])*?'

# Segmenteur RegEx Simple

def create_blocs(script: Script, texte: List[str]) -> List[Bloc]:
    '''
    Segmente texte et renvoie une liste des Blocs initialisés.
    '''

    list_blocs: List[Bloc] = []

    pattern_ligne_vide = re.compile(REGEX_LIGNE_VIDE)
    pattern_commentaire_inligne = re.compile(REGEX_TOUT + REGEX_INLINE)
    pattern_commentaire_multiligne = re.compile(REGEX_TOUT + REGEX_MULTILIGNE)
    pattern_fin_de_requete = re.compile(REGEX_TOUT + ';' + REGEX_TOUT)

    debut_statement = 0
    ligne_ag: str = ""

    for (i, ligne) in enumerate(texte, 1):

        if pattern_commentaire_inligne.match(ligne):
            # separe le commentaire du reste de la ligne et créé une instance de commentaire
            (ligne, ext_comment) = extraction_inligne(ligne)
            list_blocs.append(Commentaire(script, ext_comment, i, i, script.id + '.' + str(len(list_blocs) + 1)))

        ligne_ag += ligne

        if pattern_commentaire_multiligne.match(ligne_ag):
            (ligne_ag, ext_comment) = extraction_multiligne(ligne_ag)
            for j in ext_comment:
                list_blocs.append(Commentaire(script, j, (i - nb_lignes(j)) + 1, i, script.id + '.' + str(len(list_blocs) + 1)))

        if pattern_ligne_vide.match(ligne_ag):
            # pour l'instant on ne stocke pas les ligne vide
            ligne_ag = ""
            debut_statement = i + 1

        if pattern_fin_de_requete.match(ligne_ag):
            # stocker ou creer instance de requete
            list_blocs.append(Requete(script, ligne_ag, debut_statement, i, script.id + '.' + str(len(list_blocs) + 1)))
            ligne_ag = ""
            debut_statement = i + 1

    return list_blocs

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

def new_table(table: str = None, type_table: str = "Table") -> Table:
    t_splits = table.split(" ")

    return Table(nom=t_splits[0], alias=t_splits[-1], type_table=type_table)
