'''
Contient la classe chargée de traiter, stocker et manipuler les informations liées aux requêtes.
'''

import re

from typing import List

import sqlparse
import xlsxwriter

from sqlparse.tokens import Wildcard, Keyword, Punctuation, DDL, DML, Name, Literal
from sqlparse.sql import TokenList, Identifier, IdentifierList, Function, Operation, Parenthesis, Where

from src.classes.utils import recup_script
from src.classes.const_regex import REG_w, REG_s, REG_d, REG_S
from src.classes.table import Table
from src.classes.code import Code


class Requete(Code):
    '''
    description
    '''

    def __init__(self, texte: str, debut: int, fin: int, id_: str) -> None:
        Code.__init__(self, texte, debut, fin, id_)
        self.dict_infos = {'Variables': [], 'Functions': [], 'Var_raw': [], 'Var_def': [],
                           'list_comparaisons': [],
                           'list_references': [], 'cpt_join': 0, 'type': None}
        self.request = sqlparse.format(texte, keyword_case='upper', strip_comments=True, strip_whitespace=True)
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
        """
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
        cpt = recup_script(self.id).cpt_excel
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

        recup_script(self.id).cpt_excel = cpt

        return workbook

def new_table(table: str = None, type_table: str = "Table") -> Table:
    t_splits = table.split(" ")

    return Table(nom=t_splits[0], alias=t_splits[-1], type_table=type_table)
