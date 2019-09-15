# Generated from /home/ktant/Documents/PPL/assignment1/initial/src/main/mc/parser/MC.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22")
        buf.write("l\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\4\20\t\20\3\2\6\2\"\n\2\r\2\16\2#\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\4\3\4\5\4-\n\4\3\5\3\5\5\5\61\n\5\3\6")
        buf.write("\3\6\5\6\65\n\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3")
        buf.write("\t\3\t\3\n\3\n\3\n\5\nE\n\n\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\f\3\f\5\fP\n\f\3\r\3\r\3\r\5\rU\n\r\3\16\3")
        buf.write("\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17a\n\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\2\2")
        buf.write("\21\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36\2\4\3\2\4\5")
        buf.write("\4\2\3\3\b\t\2d\2!\3\2\2\2\4\'\3\2\2\2\6*\3\2\2\2\b\60")
        buf.write("\3\2\2\2\n\64\3\2\2\2\f\66\3\2\2\2\16:\3\2\2\2\20>\3\2")
        buf.write("\2\2\22A\3\2\2\2\24F\3\2\2\2\26M\3\2\2\2\30Q\3\2\2\2\32")
        buf.write("V\3\2\2\2\34Y\3\2\2\2\36b\3\2\2\2 \"\5\4\3\2! \3\2\2\2")
        buf.write("\"#\3\2\2\2#!\3\2\2\2#$\3\2\2\2$%\3\2\2\2%&\7\2\2\3&\3")
        buf.write("\3\2\2\2\'(\5\b\5\2()\5\6\4\2)\5\3\2\2\2*,\5\b\5\2+-\5")
        buf.write("\6\4\2,+\3\2\2\2,-\3\2\2\2-\7\3\2\2\2.\61\5\n\6\2/\61")
        buf.write("\5\24\13\2\60.\3\2\2\2\60/\3\2\2\2\61\t\3\2\2\2\62\65")
        buf.write("\5\f\7\2\63\65\5\16\b\2\64\62\3\2\2\2\64\63\3\2\2\2\65")
        buf.write("\13\3\2\2\2\66\67\7\3\2\2\678\t\2\2\289\7\6\2\29\r\3\2")
        buf.write("\2\2:;\7\3\2\2;<\5\20\t\2<=\7\6\2\2=\17\3\2\2\2>?\t\2")
        buf.write("\2\2?@\5\22\n\2@\21\3\2\2\2AB\7\7\2\2BD\t\2\2\2CE\5\22")
        buf.write("\n\2DC\3\2\2\2DE\3\2\2\2E\23\3\2\2\2FG\t\3\2\2GH\7\4\2")
        buf.write("\2HI\7\n\2\2IJ\5\26\f\2JK\7\13\2\2KL\7\f\2\2L\25\3\2\2")
        buf.write("\2MO\5\32\16\2NP\5\30\r\2ON\3\2\2\2OP\3\2\2\2P\27\3\2")
        buf.write("\2\2QR\7\7\2\2RT\5\32\16\2SU\5\30\r\2TS\3\2\2\2TU\3\2")
        buf.write("\2\2U\31\3\2\2\2VW\t\2\2\2WX\5\20\t\2X\33\3\2\2\2YZ\7")
        buf.write("\r\2\2Z[\7\n\2\2[\\\7\16\2\2\\]\7\13\2\2]`\7\17\2\2^_")
        buf.write("\7\20\2\2_a\7\17\2\2`^\3\2\2\2`a\3\2\2\2a\35\3\2\2\2b")
        buf.write("c\7\21\2\2cd\7\n\2\2de\7\22\2\2ef\7\6\2\2fg\7\16\2\2g")
        buf.write("h\7\6\2\2hi\7\22\2\2ij\7\13\2\2j\37\3\2\2\2\n#,\60\64")
        buf.write("DOT`")
        return buf.getvalue()


class MCParser ( Parser ):

    grammarFileName = "MC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "PrimiType", "ID", "ARRAYTYPE", "SEMI", 
                      "CM", "ARRAYPTTYPE", "VOIDTYPE", "LB", "RB", "Blksmt", 
                      "IF", "EXPBL", "SMT", "ELSE", "FOR", "EXPINT" ]

    RULE_program = 0
    RULE_manydecls = 1
    RULE_declTail = 2
    RULE_decl = 3
    RULE_declVar = 4
    RULE_singleDeclvar = 5
    RULE_listDeclvar = 6
    RULE_listid = 7
    RULE_idtail = 8
    RULE_declfunc = 9
    RULE_paralist = 10
    RULE_paratail = 11
    RULE_para = 12
    RULE_ifStmt = 13
    RULE_forStmt = 14

    ruleNames =  [ "program", "manydecls", "declTail", "decl", "declVar", 
                   "singleDeclvar", "listDeclvar", "listid", "idtail", "declfunc", 
                   "paralist", "paratail", "para", "ifStmt", "forStmt" ]

    EOF = Token.EOF
    PrimiType=1
    ID=2
    ARRAYTYPE=3
    SEMI=4
    CM=5
    ARRAYPTTYPE=6
    VOIDTYPE=7
    LB=8
    RB=9
    Blksmt=10
    IF=11
    EXPBL=12
    SMT=13
    ELSE=14
    FOR=15
    EXPINT=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MCParser.EOF, 0)

        def manydecls(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.ManydeclsContext)
            else:
                return self.getTypedRuleContext(MCParser.ManydeclsContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_program




    def program(self):

        localctx = MCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 30
                self.manydecls()
                self.state = 33 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.PrimiType) | (1 << MCParser.ARRAYPTTYPE) | (1 << MCParser.VOIDTYPE))) != 0)):
                    break

            self.state = 35
            self.match(MCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ManydeclsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MCParser.DeclContext,0)


        def declTail(self):
            return self.getTypedRuleContext(MCParser.DeclTailContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_manydecls




    def manydecls(self):

        localctx = MCParser.ManydeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_manydecls)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.decl()
            self.state = 38
            self.declTail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclTailContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MCParser.DeclContext,0)


        def declTail(self):
            return self.getTypedRuleContext(MCParser.DeclTailContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_declTail




    def declTail(self):

        localctx = MCParser.DeclTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declTail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.decl()
            self.state = 42
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 41
                self.declTail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declVar(self):
            return self.getTypedRuleContext(MCParser.DeclVarContext,0)


        def declfunc(self):
            return self.getTypedRuleContext(MCParser.DeclfuncContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_decl




    def decl(self):

        localctx = MCParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_decl)
        try:
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.declVar()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.declfunc()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclVarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleDeclvar(self):
            return self.getTypedRuleContext(MCParser.SingleDeclvarContext,0)


        def listDeclvar(self):
            return self.getTypedRuleContext(MCParser.ListDeclvarContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_declVar




    def declVar(self):

        localctx = MCParser.DeclVarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declVar)
        try:
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.singleDeclvar()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.listDeclvar()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SingleDeclvarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PrimiType(self):
            return self.getToken(MCParser.PrimiType, 0)

        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def ARRAYTYPE(self):
            return self.getToken(MCParser.ARRAYTYPE, 0)

        def getRuleIndex(self):
            return MCParser.RULE_singleDeclvar




    def singleDeclvar(self):

        localctx = MCParser.SingleDeclvarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_singleDeclvar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(MCParser.PrimiType)
            self.state = 53
            _la = self._input.LA(1)
            if not(_la==MCParser.ID or _la==MCParser.ARRAYTYPE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 54
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ListDeclvarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PrimiType(self):
            return self.getToken(MCParser.PrimiType, 0)

        def listid(self):
            return self.getTypedRuleContext(MCParser.ListidContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_listDeclvar




    def listDeclvar(self):

        localctx = MCParser.ListDeclvarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_listDeclvar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(MCParser.PrimiType)
            self.state = 57
            self.listid()
            self.state = 58
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ListidContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idtail(self):
            return self.getTypedRuleContext(MCParser.IdtailContext,0)


        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def ARRAYTYPE(self):
            return self.getToken(MCParser.ARRAYTYPE, 0)

        def getRuleIndex(self):
            return MCParser.RULE_listid




    def listid(self):

        localctx = MCParser.ListidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_listid)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            _la = self._input.LA(1)
            if not(_la==MCParser.ID or _la==MCParser.ARRAYTYPE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 61
            self.idtail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdtailContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(MCParser.CM, 0)

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def ARRAYTYPE(self):
            return self.getToken(MCParser.ARRAYTYPE, 0)

        def idtail(self):
            return self.getTypedRuleContext(MCParser.IdtailContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_idtail




    def idtail(self):

        localctx = MCParser.IdtailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_idtail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(MCParser.CM)
            self.state = 64
            _la = self._input.LA(1)
            if not(_la==MCParser.ID or _la==MCParser.ARRAYTYPE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 65
                self.idtail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclfuncContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def paralist(self):
            return self.getTypedRuleContext(MCParser.ParalistContext,0)


        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def Blksmt(self):
            return self.getToken(MCParser.Blksmt, 0)

        def PrimiType(self):
            return self.getToken(MCParser.PrimiType, 0)

        def ARRAYPTTYPE(self):
            return self.getToken(MCParser.ARRAYPTTYPE, 0)

        def VOIDTYPE(self):
            return self.getToken(MCParser.VOIDTYPE, 0)

        def getRuleIndex(self):
            return MCParser.RULE_declfunc




    def declfunc(self):

        localctx = MCParser.DeclfuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_declfunc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.PrimiType) | (1 << MCParser.ARRAYPTTYPE) | (1 << MCParser.VOIDTYPE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 69
            self.match(MCParser.ID)
            self.state = 70
            self.match(MCParser.LB)
            self.state = 71
            self.paralist()
            self.state = 72
            self.match(MCParser.RB)
            self.state = 73
            self.match(MCParser.Blksmt)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParalistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def para(self):
            return self.getTypedRuleContext(MCParser.ParaContext,0)


        def paratail(self):
            return self.getTypedRuleContext(MCParser.ParatailContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_paralist




    def paralist(self):

        localctx = MCParser.ParalistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_paralist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.para()
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.CM:
                self.state = 76
                self.paratail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParatailContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(MCParser.CM, 0)

        def para(self):
            return self.getTypedRuleContext(MCParser.ParaContext,0)


        def paratail(self):
            return self.getTypedRuleContext(MCParser.ParatailContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_paratail




    def paratail(self):

        localctx = MCParser.ParatailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_paratail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(MCParser.CM)
            self.state = 80
            self.para()
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.CM:
                self.state = 81
                self.paratail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listid(self):
            return self.getTypedRuleContext(MCParser.ListidContext,0)


        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def ARRAYTYPE(self):
            return self.getToken(MCParser.ARRAYTYPE, 0)

        def getRuleIndex(self):
            return MCParser.RULE_para




    def para(self):

        localctx = MCParser.ParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_para)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            _la = self._input.LA(1)
            if not(_la==MCParser.ID or _la==MCParser.ARRAYTYPE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 85
            self.listid()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IfStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MCParser.IF, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def EXPBL(self):
            return self.getToken(MCParser.EXPBL, 0)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def SMT(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.SMT)
            else:
                return self.getToken(MCParser.SMT, i)

        def ELSE(self):
            return self.getToken(MCParser.ELSE, 0)

        def getRuleIndex(self):
            return MCParser.RULE_ifStmt




    def ifStmt(self):

        localctx = MCParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(MCParser.IF)
            self.state = 88
            self.match(MCParser.LB)
            self.state = 89
            self.match(MCParser.EXPBL)
            self.state = 90
            self.match(MCParser.RB)
            self.state = 91
            self.match(MCParser.SMT)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.ELSE:
                self.state = 92
                self.match(MCParser.ELSE)
                self.state = 93
                self.match(MCParser.SMT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ForStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MCParser.FOR, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def EXPINT(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.EXPINT)
            else:
                return self.getToken(MCParser.EXPINT, i)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.SEMI)
            else:
                return self.getToken(MCParser.SEMI, i)

        def EXPBL(self):
            return self.getToken(MCParser.EXPBL, 0)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_forStmt




    def forStmt(self):

        localctx = MCParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_forStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(MCParser.FOR)
            self.state = 97
            self.match(MCParser.LB)
            self.state = 98
            self.match(MCParser.EXPINT)
            self.state = 99
            self.match(MCParser.SEMI)
            self.state = 100
            self.match(MCParser.EXPBL)
            self.state = 101
            self.match(MCParser.SEMI)
            self.state = 102
            self.match(MCParser.EXPINT)
            self.state = 103
            self.match(MCParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





