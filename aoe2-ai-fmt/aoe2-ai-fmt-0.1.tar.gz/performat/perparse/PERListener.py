# Generated from PER.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PERParser import PERParser
else:
    from PERParser import PERParser

# This class defines a complete listener for a parse tree produced by PERParser.
class PERListener(ParseTreeListener):

    # Enter a parse tree produced by PERParser#per.
    def enterPer(self, ctx:PERParser.PerContext):
        pass

    # Exit a parse tree produced by PERParser#per.
    def exitPer(self, ctx:PERParser.PerContext):
        pass


    # Enter a parse tree produced by PERParser#toplevel_content.
    def enterToplevel_content(self, ctx:PERParser.Toplevel_contentContext):
        pass

    # Exit a parse tree produced by PERParser#toplevel_content.
    def exitToplevel_content(self, ctx:PERParser.Toplevel_contentContext):
        pass


    # Enter a parse tree produced by PERParser#conditional_block.
    def enterConditional_block(self, ctx:PERParser.Conditional_blockContext):
        pass

    # Exit a parse tree produced by PERParser#conditional_block.
    def exitConditional_block(self, ctx:PERParser.Conditional_blockContext):
        pass


    # Enter a parse tree produced by PERParser#conditional_cond.
    def enterConditional_cond(self, ctx:PERParser.Conditional_condContext):
        pass

    # Exit a parse tree produced by PERParser#conditional_cond.
    def exitConditional_cond(self, ctx:PERParser.Conditional_condContext):
        pass


    # Enter a parse tree produced by PERParser#conditional_content.
    def enterConditional_content(self, ctx:PERParser.Conditional_contentContext):
        pass

    # Exit a parse tree produced by PERParser#conditional_content.
    def exitConditional_content(self, ctx:PERParser.Conditional_contentContext):
        pass


    # Enter a parse tree produced by PERParser#conditional_else.
    def enterConditional_else(self, ctx:PERParser.Conditional_elseContext):
        pass

    # Exit a parse tree produced by PERParser#conditional_else.
    def exitConditional_else(self, ctx:PERParser.Conditional_elseContext):
        pass


    # Enter a parse tree produced by PERParser#statement.
    def enterStatement(self, ctx:PERParser.StatementContext):
        pass

    # Exit a parse tree produced by PERParser#statement.
    def exitStatement(self, ctx:PERParser.StatementContext):
        pass


    # Enter a parse tree produced by PERParser#lone_comment.
    def enterLone_comment(self, ctx:PERParser.Lone_commentContext):
        pass

    # Exit a parse tree produced by PERParser#lone_comment.
    def exitLone_comment(self, ctx:PERParser.Lone_commentContext):
        pass


    # Enter a parse tree produced by PERParser#command.
    def enterCommand(self, ctx:PERParser.CommandContext):
        pass

    # Exit a parse tree produced by PERParser#command.
    def exitCommand(self, ctx:PERParser.CommandContext):
        pass


    # Enter a parse tree produced by PERParser#defrule.
    def enterDefrule(self, ctx:PERParser.DefruleContext):
        pass

    # Exit a parse tree produced by PERParser#defrule.
    def exitDefrule(self, ctx:PERParser.DefruleContext):
        pass


    # Enter a parse tree produced by PERParser#proposition_list.
    def enterProposition_list(self, ctx:PERParser.Proposition_listContext):
        pass

    # Exit a parse tree produced by PERParser#proposition_list.
    def exitProposition_list(self, ctx:PERParser.Proposition_listContext):
        pass


    # Enter a parse tree produced by PERParser#proposition.
    def enterProposition(self, ctx:PERParser.PropositionContext):
        pass

    # Exit a parse tree produced by PERParser#proposition.
    def exitProposition(self, ctx:PERParser.PropositionContext):
        pass


    # Enter a parse tree produced by PERParser#proposition_arg.
    def enterProposition_arg(self, ctx:PERParser.Proposition_argContext):
        pass

    # Exit a parse tree produced by PERParser#proposition_arg.
    def exitProposition_arg(self, ctx:PERParser.Proposition_argContext):
        pass


    # Enter a parse tree produced by PERParser#action_list.
    def enterAction_list(self, ctx:PERParser.Action_listContext):
        pass

    # Exit a parse tree produced by PERParser#action_list.
    def exitAction_list(self, ctx:PERParser.Action_listContext):
        pass


    # Enter a parse tree produced by PERParser#action.
    def enterAction(self, ctx:PERParser.ActionContext):
        pass

    # Exit a parse tree produced by PERParser#action.
    def exitAction(self, ctx:PERParser.ActionContext):
        pass


    # Enter a parse tree produced by PERParser#action_arg.
    def enterAction_arg(self, ctx:PERParser.Action_argContext):
        pass

    # Exit a parse tree produced by PERParser#action_arg.
    def exitAction_arg(self, ctx:PERParser.Action_argContext):
        pass


    # Enter a parse tree produced by PERParser#defconst.
    def enterDefconst(self, ctx:PERParser.DefconstContext):
        pass

    # Exit a parse tree produced by PERParser#defconst.
    def exitDefconst(self, ctx:PERParser.DefconstContext):
        pass


    # Enter a parse tree produced by PERParser#load.
    def enterLoad(self, ctx:PERParser.LoadContext):
        pass

    # Exit a parse tree produced by PERParser#load.
    def exitLoad(self, ctx:PERParser.LoadContext):
        pass


    # Enter a parse tree produced by PERParser#load_random_list.
    def enterLoad_random_list(self, ctx:PERParser.Load_random_listContext):
        pass

    # Exit a parse tree produced by PERParser#load_random_list.
    def exitLoad_random_list(self, ctx:PERParser.Load_random_listContext):
        pass


    # Enter a parse tree produced by PERParser#random_file_list.
    def enterRandom_file_list(self, ctx:PERParser.Random_file_listContext):
        pass

    # Exit a parse tree produced by PERParser#random_file_list.
    def exitRandom_file_list(self, ctx:PERParser.Random_file_listContext):
        pass


    # Enter a parse tree produced by PERParser#random_file.
    def enterRandom_file(self, ctx:PERParser.Random_fileContext):
        pass

    # Exit a parse tree produced by PERParser#random_file.
    def exitRandom_file(self, ctx:PERParser.Random_fileContext):
        pass


    # Enter a parse tree produced by PERParser#whitespace_comment.
    def enterWhitespace_comment(self, ctx:PERParser.Whitespace_commentContext):
        pass

    # Exit a parse tree produced by PERParser#whitespace_comment.
    def exitWhitespace_comment(self, ctx:PERParser.Whitespace_commentContext):
        pass



del PERParser