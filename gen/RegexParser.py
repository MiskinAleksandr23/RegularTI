# Generated from /Users/near/RegularTI/grammar/Regex.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys

if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4, 1, 8, 45, 2, 0, 7, 0, 2, 1, 7, 1, 2, 2, 7, 2, 2, 3, 7, 3, 2, 4, 7, 4, 2, 5, 7, 5, 2, 6, 7, 6,
        1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 5, 1, 21, 8, 1, 10, 1, 12, 1, 24, 9, 1, 1, 2, 4, 2, 27, 8,
        2, 11, 2, 12, 2, 28, 1, 3, 1, 3, 3, 3, 33, 8, 3, 1, 4, 1, 4, 3, 4, 37, 8, 4, 1, 5, 1, 5, 1, 5,
        1, 5, 1, 6, 1, 6, 1, 6, 0, 0, 7, 0, 2, 4, 6, 8, 10, 12, 0, 1, 1, 0, 4, 6, 41, 0, 14, 1, 0, 0,
        0, 2, 17, 1, 0, 0, 0, 4, 26, 1, 0, 0, 0, 6, 30, 1, 0, 0, 0, 8, 36, 1, 0, 0, 0, 10, 38, 1, 0,
        0, 0, 12, 42, 1, 0, 0, 0, 14, 15, 3, 2, 1, 0, 15, 16, 5, 0, 0, 1, 16, 1, 1, 0, 0, 0, 17, 22,
        3, 4, 2, 0, 18, 19, 5, 7, 0, 0, 19, 21, 3, 4, 2, 0, 20, 18, 1, 0, 0, 0, 21, 24, 1, 0, 0, 0,
        22, 20, 1, 0, 0, 0, 22, 23, 1, 0, 0, 0, 23, 3, 1, 0, 0, 0, 24, 22, 1, 0, 0, 0, 25, 27, 3, 6,
        3, 0, 26, 25, 1, 0, 0, 0, 27, 28, 1, 0, 0, 0, 28, 26, 1, 0, 0, 0, 28, 29, 1, 0, 0, 0, 29, 5,
        1, 0, 0, 0, 30, 32, 3, 8, 4, 0, 31, 33, 7, 0, 0, 0, 32, 31, 1, 0, 0, 0, 32, 33, 1, 0, 0, 0,
        33, 7, 1, 0, 0, 0, 34, 37, 3, 10, 5, 0, 35, 37, 3, 12, 6, 0, 36, 34, 1, 0, 0, 0, 36, 35, 1,
        0, 0, 0, 37, 9, 1, 0, 0, 0, 38, 39, 5, 1, 0, 0, 39, 40, 3, 2, 1, 0, 40, 41, 5, 2, 0, 0, 41,
        11, 1, 0, 0, 0, 42, 43, 5, 3, 0, 0, 43, 13, 1, 0, 0, 0, 4, 22, 28, 32, 36
    ]


class RegexParser(Parser):
    grammarFileName = "Regex.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "'('", "')'", "<INVALID>", "'*'", "'+'",
                    "'?'", "'|'"]

    symbolicNames = ["<INVALID>", "<INVALID>", "<INVALID>", "CHAR", "STAR",
                     "PLUS", "QUESTION", "PIPE", "WS"]

    RULE_regex = 0
    RULE_alternation = 1
    RULE_concatenation = 2
    RULE_repetition = 3
    RULE_primary = 4
    RULE_group = 5
    RULE_symbol = 6

    ruleNames = ["regex", "alternation", "concatenation", "repetition",
                 "primary", "group", "symbol"]

    EOF = Token.EOF
    T__0 = 1
    T__1 = 2
    CHAR = 3
    STAR = 4
    PLUS = 5
    QUESTION = 6
    PIPE = 7
    WS = 8

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

    class RegexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def alternation(self):
            return self.getTypedRuleContext(RegexParser.AlternationContext, 0)

        def EOF(self):
            return self.getToken(RegexParser.EOF, 0)

        def getRuleIndex(self):
            return RegexParser.RULE_regex

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterRegex"):
                listener.enterRegex(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitRegex"):
                listener.exitRegex(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitRegex"):
                return visitor.visitRegex(self)
            else:
                return visitor.visitChildren(self)

    def regex(self):

        localctx = RegexParser.RegexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_regex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.alternation()
            self.state = 15
            self.match(RegexParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AlternationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def concatenation(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(RegexParser.ConcatenationContext)
            else:
                return self.getTypedRuleContext(RegexParser.ConcatenationContext, i)

        def PIPE(self, i: int = None):
            if i is None:
                return self.getTokens(RegexParser.PIPE)
            else:
                return self.getToken(RegexParser.PIPE, i)

        def getRuleIndex(self):
            return RegexParser.RULE_alternation

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterAlternation"):
                listener.enterAlternation(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitAlternation"):
                listener.exitAlternation(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAlternation"):
                return visitor.visitAlternation(self)
            else:
                return visitor.visitChildren(self)

    def alternation(self):

        localctx = RegexParser.AlternationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_alternation)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.concatenation()
            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 7:
                self.state = 18
                self.match(RegexParser.PIPE)
                self.state = 19
                self.concatenation()
                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConcatenationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def repetition(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(RegexParser.RepetitionContext)
            else:
                return self.getTypedRuleContext(RegexParser.RepetitionContext, i)

        def getRuleIndex(self):
            return RegexParser.RULE_concatenation

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterConcatenation"):
                listener.enterConcatenation(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitConcatenation"):
                listener.exitConcatenation(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitConcatenation"):
                return visitor.visitConcatenation(self)
            else:
                return visitor.visitChildren(self)

    def concatenation(self):

        localctx = RegexParser.ConcatenationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_concatenation)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 25
                self.repetition()
                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la == 1 or _la == 3):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RepetitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self):
            return self.getTypedRuleContext(RegexParser.PrimaryContext, 0)

        def STAR(self):
            return self.getToken(RegexParser.STAR, 0)

        def PLUS(self):
            return self.getToken(RegexParser.PLUS, 0)

        def QUESTION(self):
            return self.getToken(RegexParser.QUESTION, 0)

        def getRuleIndex(self):
            return RegexParser.RULE_repetition

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterRepetition"):
                listener.enterRepetition(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitRepetition"):
                listener.exitRepetition(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitRepetition"):
                return visitor.visitRepetition(self)
            else:
                return visitor.visitChildren(self)

    def repetition(self):

        localctx = RegexParser.RepetitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_repetition)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.primary()
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 112) != 0):
                self.state = 31
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 112) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def group(self):
            return self.getTypedRuleContext(RegexParser.GroupContext, 0)

        def symbol(self):
            return self.getTypedRuleContext(RegexParser.SymbolContext, 0)

        def getRuleIndex(self):
            return RegexParser.RULE_primary

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterPrimary"):
                listener.enterPrimary(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitPrimary"):
                listener.exitPrimary(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitPrimary"):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)

    def primary(self):

        localctx = RegexParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_primary)
        try:
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.group()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.symbol()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GroupContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def alternation(self):
            return self.getTypedRuleContext(RegexParser.AlternationContext, 0)

        def getRuleIndex(self):
            return RegexParser.RULE_group

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterGroup"):
                listener.enterGroup(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitGroup"):
                listener.exitGroup(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitGroup"):
                return visitor.visitGroup(self)
            else:
                return visitor.visitChildren(self)

    def group(self):

        localctx = RegexParser.GroupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_group)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(RegexParser.T__0)
            self.state = 39
            self.alternation()
            self.state = 40
            self.match(RegexParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SymbolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHAR(self):
            return self.getToken(RegexParser.CHAR, 0)

        def getRuleIndex(self):
            return RegexParser.RULE_symbol

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterSymbol"):
                listener.enterSymbol(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitSymbol"):
                listener.exitSymbol(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitSymbol"):
                return visitor.visitSymbol(self)
            else:
                return visitor.visitChildren(self)

    def symbol(self):

        localctx = RegexParser.SymbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_symbol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(RegexParser.CHAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
