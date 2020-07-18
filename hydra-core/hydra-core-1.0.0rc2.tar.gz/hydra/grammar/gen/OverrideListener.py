# Generated from /home/omry/dev/hydra/hydra/grammar/Override.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .OverrideParser import OverrideParser
else:
    from OverrideParser import OverrideParser

# This class defines a complete listener for a parse tree produced by OverrideParser.
class OverrideListener(ParseTreeListener):

    # Enter a parse tree produced by OverrideParser#override.
    def enterOverride(self, ctx:OverrideParser.OverrideContext):
        pass

    # Exit a parse tree produced by OverrideParser#override.
    def exitOverride(self, ctx:OverrideParser.OverrideContext):
        pass


    # Enter a parse tree produced by OverrideParser#key.
    def enterKey(self, ctx:OverrideParser.KeyContext):
        pass

    # Exit a parse tree produced by OverrideParser#key.
    def exitKey(self, ctx:OverrideParser.KeyContext):
        pass


    # Enter a parse tree produced by OverrideParser#packageOrGroup.
    def enterPackageOrGroup(self, ctx:OverrideParser.PackageOrGroupContext):
        pass

    # Exit a parse tree produced by OverrideParser#packageOrGroup.
    def exitPackageOrGroup(self, ctx:OverrideParser.PackageOrGroupContext):
        pass


    # Enter a parse tree produced by OverrideParser#package.
    def enterPackage(self, ctx:OverrideParser.PackageContext):
        pass

    # Exit a parse tree produced by OverrideParser#package.
    def exitPackage(self, ctx:OverrideParser.PackageContext):
        pass


    # Enter a parse tree produced by OverrideParser#value.
    def enterValue(self, ctx:OverrideParser.ValueContext):
        pass

    # Exit a parse tree produced by OverrideParser#value.
    def exitValue(self, ctx:OverrideParser.ValueContext):
        pass


    # Enter a parse tree produced by OverrideParser#element.
    def enterElement(self, ctx:OverrideParser.ElementContext):
        pass

    # Exit a parse tree produced by OverrideParser#element.
    def exitElement(self, ctx:OverrideParser.ElementContext):
        pass


    # Enter a parse tree produced by OverrideParser#choiceSweep.
    def enterChoiceSweep(self, ctx:OverrideParser.ChoiceSweepContext):
        pass

    # Exit a parse tree produced by OverrideParser#choiceSweep.
    def exitChoiceSweep(self, ctx:OverrideParser.ChoiceSweepContext):
        pass


    # Enter a parse tree produced by OverrideParser#primitive.
    def enterPrimitive(self, ctx:OverrideParser.PrimitiveContext):
        pass

    # Exit a parse tree produced by OverrideParser#primitive.
    def exitPrimitive(self, ctx:OverrideParser.PrimitiveContext):
        pass


    # Enter a parse tree produced by OverrideParser#listValue.
    def enterListValue(self, ctx:OverrideParser.ListValueContext):
        pass

    # Exit a parse tree produced by OverrideParser#listValue.
    def exitListValue(self, ctx:OverrideParser.ListValueContext):
        pass


    # Enter a parse tree produced by OverrideParser#dictValue.
    def enterDictValue(self, ctx:OverrideParser.DictValueContext):
        pass

    # Exit a parse tree produced by OverrideParser#dictValue.
    def exitDictValue(self, ctx:OverrideParser.DictValueContext):
        pass


    # Enter a parse tree produced by OverrideParser#id_ws.
    def enterId_ws(self, ctx:OverrideParser.Id_wsContext):
        pass

    # Exit a parse tree produced by OverrideParser#id_ws.
    def exitId_ws(self, ctx:OverrideParser.Id_wsContext):
        pass



del OverrideParser