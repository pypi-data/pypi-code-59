import os

import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'IMPORT',
    'FROM',
    'NAME',
    'COLON',
    'OR',
    'LBRACE',
    'RBRACE',
    'COMMA',
    'STRING',
    'DSTRING',
    'EQUAL',
    'NEWLINE',
    'INT',
    'COMMENT'
)

t_COLON = r':'
t_OR = r'\|'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_COMMA = r','
t_NEWLINE = r'\n'
t_EQUAL = r'='
t_ignore = r'[ ]'


def t_IMPORT(t):
    r'import'
    t.type = 'IMPORT'
    return t


def t_FROM(t):
    r'from'
    t.type = 'FROM'
    return t


def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = 'NAME'
    return t


def t_STRING(t):
    r'\'.*?\''
    t.type = 'STRING'
    t.value = t.value[1:-1]
    return t


def t_DSTRING(t):
    r'\".*?\"'
    t.type = 'STRING'
    t.value = t.value[1:-1]
    return t


def t_INT(t):
    r'\d+'
    t.type = 'INT'
    t.value = int(t.value)
    return t


def t_COMMENT(t):
    r'\# .*?\n'
    t.type = 'COMMENT'
    return t


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex.lex()


def run_lex(content):
    lexer.input(content)
    return lexer


def p_main_01(p):
    '''
    main : break imports grammar
    '''
    p[0] = p[3]
    p[0]['imports'] = p[2]['imports']


def p_main_02(p):
    '''
    main : imports grammar
    '''
    p[0] = p[2]
    p[0]['imports'] = p[1]['imports']


def p_main_03(p):
    '''
    main : break grammar
    '''
    p[0] = p[2]


def p_main_04(p):
    '''
    main : grammar
    '''
    p[0] = p[1]


def p_main_05(p):
    '''
    main : imports
    '''
    p[0] = p[1]


def p_grammar_import(p):
    '''
    imports : import_statement imports
            | import_statement
    '''
    p[0] = p[2] if len(p) == 3 else {}

    imports = p[0]['imports'] if 'imports' in p[0] else []
    imports.insert(0, p[1])
    p[0]['imports'] = imports


def p_declaration(p):
    '''
    grammar : NAME EQUAL json break grammar
            | NAME EQUAL json break
    '''
    if len(p) == 6:
        p[0] = p[5]
    else:
        p[0] = {}

    definitions = p[0]['definitions'] if 'definitions' in p[0] else {}

    # Check if not already set so we force using the latest
    if p[1] not in definitions:
        definitions[p[1]] = p[3]

    p[0]['definitions'] = definitions


def p_grammar_productions(p):
    '''
    grammar : production grammar
            | production
    '''
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = {}

    productionRules = p[0]['productionRules'] if 'productionRules' in p[0] else {}

    # Check if not already set so we force using the latest
    if p[1][0] not in productionRules:
        productionRules[p[1][0]] = p[1][1]

    p[0]['productionRules'] = productionRules


def p_import_statement(p):
    '''
    import_statement : IMPORT import_list FROM STRING break
    '''
    p[0] = {
        "source": p[4],
        "names": p[2]
    }


def p_import_list(p):
    '''
    import_list : NAME COMMA break import_list
               | NAME COMMA import_list
               | NAME
    '''
    p[0] = []
    if len(p) == 5:
        p[0] = p[4]
    elif len(p) == 4:
        p[0] = p[3]

    p[0].append(p[1])


def p_production(p):
    '''
    production : NAME COLON production_tokens
    '''
    p[0] = (p[1], p[3])


def p_production_tokens_with_newline(p):
    '''
    production_tokens : token_list break OR production_tokens
                      | token_list OR production_tokens
                      | token_list break
    '''
    tokens = [
        {
            'tokens': p[1][0]
        }
    ]

    if p[1][1]:
        tokens[0]['action'] = p[1][1]

    if len(p) == 3:
        p[0] = tokens
    elif len(p) == 4:
        p[0] = tokens + p[3]
    else:
        p[0] = tokens + p[4]


def p_token_list(p):
    '''
    token_list : NAME token_list
    '''
    p[0] = ([p[1]] if len(p) == 2 else [p[1]] + p[2][0], p[2][1])


def p_token_list_tail_with_action(p):
    '''
    token_list : NAME json
    '''
    p[0] = ([p[1]], p[2])


def p_token_list_tail_no_action(p):
    '''
    token_list : NAME
    '''
    p[0] = ([p[1]], None)


def p_json(p):
    '''
    json : LBRACE fields RBRACE
         | LBRACE break fields RBRACE
    '''
    p[0] = p[2] if len(p) == 4 else p[3]


def p_fields(p):
    '''
    fields : key COLON value COMMA break fields
           | key COLON value COMMA fields
           | key COLON value break
           | key COLON value
    '''

    p[0] = {}
    if len(p) > 5:
        p[0] = p[5] if len(p) == 6 else p[6]

    # Check if not already set so we force using the latest
    if p[1] not in p[0]:
        p[0][p[1]] = p[3]


def p_key(p):
    '''
    key : STRING
        | DSTRING
        | NAME
    '''
    p[0] = p[1]


def p_value(p):
    '''
    value : STRING
          | DSTRING
          | INT
    '''
    p[0] = p[1]


def p_line_break(p):
    '''
    break : COMMENT break
          | NEWLINE break
          | COMMENT
          | NEWLINE
    '''
    pass


def p_error(p):
    print(f"Syntax error in input! {p}")


parser = yacc.yacc()


def parse(path):
    path = os.path.abspath(path)
    with open(path, 'r') as file:
        grammar_text = file.read()

    return parser.parse(input=grammar_text)
