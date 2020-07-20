"""
\node[] at () {};
\node[] at () {};
"""
import pyparsing as pp
from pyparsing import *

colon = Char(":")
selon = Char(";") # Contraction of semi-colon
comma = Char(",")
point = Char("-")

charge = Word("+-", max=1)
equals = Literal("=")

number = Word(nums + '.')
# digits = Word(nums + '.') # Char("0") | Char("1") | Char("2") | Char("3") | Char("4") | Char("5") | Char("6") | Char("7") | Char("8") | Char("9")
# Rset = Group(OneOrMore(digits) + point + OneOrMore(digits)) | OneOrMore(digits)
length = Literal("pt") | Literal("cm")
units = length
dimension = Group(Optional(charge).setResultsName("sign") + number.setResultsName("value") + Optional(length).setResultsName("units"))

print(dimension.setResultsName("dimension").parseString("3").asDict())
print(dimension.parseString("32.15"))
print(dimension.parseString("+3"))
print(dimension.parseString("-23 cm"))
print(dimension.parseString("-3.15pt"))

init_curve, term_curve = Char("("), Char(")")
init_brace, term_brace = Char("{"), Char("}")
init_block, term_block = Char("["), Char("]")

label = init_curve.suppress() + ZeroOrMore(Word(alphanums)).setResultsName("label") + term_curve.suppress()

print(label.parseString("(B)"))
print(label.parseString("(test a label)").asDict())

# coordinate = Group(init_curve.suppress() + dimension.setResultsName('x') + comma.suppress() + dimension.setResultsName("y") + term_curve.suppress()).setResultsName("co-ordinate")
coordinate_cartesian  = init_curve.suppress() + delimitedList(dimension.setResultsName('cartesian*'), ",") + term_curve.suppress()

print(coordinate_cartesian.parseString("(3,3)"))
print(coordinate_cartesian.parseString("(32.15,32.15)"))
print(coordinate_cartesian.parseString("(+3,-2)"))
print(coordinate_cartesian.parseString("(-23 cm,-23 cm)"))
print(coordinate_cartesian.parseString("(-3.15pt,-3.15pt)").asDict())

coordinate_polar      = init_curve.suppress() + dimension.setResultsName("polar*") + colon.suppress() + dimension.setResultsName("polar*") + term_curve.suppress()

print(coordinate_polar.parseString("(-3.15pt:-3.15pt)"))
print(coordinate_polar.parseString("(-3.15pt:-3.15pt)").asDict())

coordinate_coordinate = init_curve.suppress() + dimension.setResultsName("polar*") + colon.suppress() + dimension.setResultsName("polar*") + term_curve.suppress()

print(coordinate_polar.parseString("(-3.15pt:-3.15pt)"))
print(coordinate_polar.parseString("(-3.15pt:-3.15pt)").asDict())

coordinate = coordinate_cartesian | coordinate_polar | coordinate_coordinate

# TODO : Apply parser actions here
assign = Group((OneOrMore(Word(alphanums))).setResultsName("key") + Literal("=").suppress() + (OneOrMore(Word(alphanums))).setResultsName("value"))
# Originally :
# assign = Dict(Group(OneOrMore(Word(alphanums)) + Literal("=").suppress() + OneOrMore(Word(alphanums))))# ("assign")
# setting = Word(alphanums) + equals + Word(alphanums)
# assign = dictOf(OneOrMore(Word(alphanums)), Literal("=").suppress() + OneOrMore(Word(alphanums)))
# assign = Combine(OneOrMore(Word(alphanums))).setResultsName("option") + equals.suppress() + Combine(OneOrMore(Word(alphanums))).setResultsName("value")
option = Group(OneOrMore(Word(alphanums))) # Can't seem to use Combine here
# Originally :
# trigger = Word(alphanums)

print(option.setResultsName("option").parseString("yellow").asDict())
print(assign.parseString("red = blue").asDict())

options = init_block.suppress() + delimitedList(assign.setName("assign").setResultsName("options*")|option.setName("option").setResultsName("options*"), ",") + term_block.suppress()

print(options.parseString("[red]").asDict())
print(options.parseString("[fill=blue]").asDict())
print(options.parseString("[red, thin, dashed line]"))
print(options.parseString("[red, weight=2]"))
print(options.parseString("[red, fill=blue, fill=blue]").asDict())
print(options.parseString("[rotate=45, rounded corners]"))
print(options.parseString("[rotate=45, rounded corners]").asDict())
print(options.parseString("[draw, fill=blue, rounded corners]").asDict())

# for option in options.parseString("[draw, fill=blue, rounded corners]") :
#     if option.getName() == "assign" :
#         print(option.asDict())
#     else :
#         print(option)

argument = init_brace.suppress() + ZeroOrMore(Word(alphanums)).setResultsName("content") + term_brace.suppress()

print(argument.parseString("{A}"))
print(argument.parseString("{test an argument}").asDict())

node = Literal("node").suppress() + Optional(options) + Optional(label) + Optional(Literal("at").suppress() + coordinate_cartesian) + argument

print(node.parseString("node {test}"))
print(node.parseString("node {test}").asDict())
print(node.parseString("node (name) {test}"))
print(node.parseString("node (name) {test}").asDict())
print(node.parseString("node (name) at(2,4) {test}"))
print(node.parseString("node (name) at (2,-4) {test}").asDict())
print(node.parseString("node[fill=blue] at(2,4) {test}"))
print(node.parseString("node[fill=blue] at (2,-4) {test}").asDict())

# line = Literal("|-") | Literal("--") | Literal("-|");
# label|coordinate

path = Literal("\\").suppress() + Group(node).setResultsName("node") + selon.suppress()

print(path.parseString("\\node[fill=blue] at(2,-4) {test};"))
print(path.parseString("\\node[fill=blue] at (2,-4) {test};").asDict())
print(path.parseString("\\node[fill=blue, above right = of A] at(2,-4) {test};"))
print(path.parseString("\\node[fill=blue, above right = of A] at (2,-4) {test};").asDict())

# Output Generation

item = tikz = path.parseString("\\node[fill=blue, above right = of A] (A) at (2,-4) {test};").asDict()
# for path in tikz :
#     for item in path :
node = item["node"]

tikzParser = path.parseString

