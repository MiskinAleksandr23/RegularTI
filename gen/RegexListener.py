# Generated from /Users/near/RegularTI/grammar/Regex.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RegexParser import RegexParser
else:
    from RegexParser import RegexParser

# This class defines a complete listener for a parse tree produced by RegexParser.
class RegexListener(ParseTreeListener):

    # Enter a parse tree produced by RegexParser#regex.
    def enterRegex(self, ctx:RegexParser.RegexContext):
        pass

    # Exit a parse tree produced by RegexParser#regex.
    def exitRegex(self, ctx:RegexParser.RegexContext):
        pass


    # Enter a parse tree produced by RegexParser#alternation.
    def enterAlternation(self, ctx:RegexParser.AlternationContext):
        pass

    # Exit a parse tree produced by RegexParser#alternation.
    def exitAlternation(self, ctx:RegexParser.AlternationContext):
        pass


    # Enter a parse tree produced by RegexParser#concatenation.
    def enterConcatenation(self, ctx:RegexParser.ConcatenationContext):
        pass

    # Exit a parse tree produced by RegexParser#concatenation.
    def exitConcatenation(self, ctx:RegexParser.ConcatenationContext):
        pass


    # Enter a parse tree produced by RegexParser#repetition.
    def enterRepetition(self, ctx:RegexParser.RepetitionContext):
        pass

    # Exit a parse tree produced by RegexParser#repetition.
    def exitRepetition(self, ctx:RegexParser.RepetitionContext):
        pass


    # Enter a parse tree produced by RegexParser#primary.
    def enterPrimary(self, ctx:RegexParser.PrimaryContext):
        pass

    # Exit a parse tree produced by RegexParser#primary.
    def exitPrimary(self, ctx:RegexParser.PrimaryContext):
        pass


    # Enter a parse tree produced by RegexParser#group.
    def enterGroup(self, ctx:RegexParser.GroupContext):
        pass

    # Exit a parse tree produced by RegexParser#group.
    def exitGroup(self, ctx:RegexParser.GroupContext):
        pass


    # Enter a parse tree produced by RegexParser#symbol.
    def enterSymbol(self, ctx:RegexParser.SymbolContext):
        pass

    # Exit a parse tree produced by RegexParser#symbol.
    def exitSymbol(self, ctx:RegexParser.SymbolContext):
        pass



del RegexParser