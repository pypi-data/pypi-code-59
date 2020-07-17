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
