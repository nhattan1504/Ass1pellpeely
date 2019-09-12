# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\61")
        buf.write("\u012f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\7\22\u00c3\n\22\f\22\16\22\u00c6\13\22\3\23")
        buf.write("\3\23\3\24\3\24\3\25\6\25\u00cd\n\25\r\25\16\25\u00ce")
        buf.write("\3\26\3\26\5\26\u00d3\n\26\3\26\3\26\3\26\5\26\u00d8\n")
        buf.write("\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27")
        buf.write("\u00e3\n\27\3\30\3\30\5\30\u00e7\n\30\3\30\3\30\3\31\3")
        buf.write("\31\5\31\u00ed\n\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3\"")
        buf.write("\3\"\3#\3#\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3(\3")
        buf.write(")\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61")
        buf.write("\6\61\u0124\n\61\r\61\16\61\u0125\3\61\3\61\3\62\3\62")
        buf.write("\3\63\3\63\3\64\3\64\2\2\65\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\2\'\2)\24+\25-\2/\2\61\26\63\27\65\30\67\319\32;\33")
        buf.write("=\34?\35A\36C\37E G!I\"K#M$O%Q&S\'U(W)Y*[+],_-a.c/e\60")
        buf.write("g\61\3\2\7\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\4\2GGgg\5")
        buf.write("\2\13\f\17\17\"\"\2\u0133\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write("\2!\3\2\2\2\2#\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2\61\3\2")
        buf.write("\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2")
        buf.write("\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2")
        buf.write("\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2")
        buf.write("\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3")
        buf.write("\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a")
        buf.write("\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\3i\3\2\2\2\5")
        buf.write("n\3\2\2\2\7r\3\2\2\2\tw\3\2\2\2\13\177\3\2\2\2\r\u008a")
        buf.write("\3\2\2\2\17\u008e\3\2\2\2\21\u0091\3\2\2\2\23\u0096\3")
        buf.write("\2\2\2\25\u009b\3\2\2\2\27\u00a2\3\2\2\2\31\u00a8\3\2")
        buf.write("\2\2\33\u00b0\3\2\2\2\35\u00b2\3\2\2\2\37\u00b5\3\2\2")
        buf.write("\2!\u00ba\3\2\2\2#\u00c0\3\2\2\2%\u00c7\3\2\2\2\'\u00c9")
        buf.write("\3\2\2\2)\u00cc\3\2\2\2+\u00d7\3\2\2\2-\u00e2\3\2\2\2")
        buf.write("/\u00e4\3\2\2\2\61\u00ec\3\2\2\2\63\u00ee\3\2\2\2\65\u00f0")
        buf.write("\3\2\2\2\67\u00f2\3\2\2\29\u00f4\3\2\2\2;\u00f7\3\2\2")
        buf.write("\2=\u00fa\3\2\2\2?\u00fc\3\2\2\2A\u00ff\3\2\2\2C\u0101")
        buf.write("\3\2\2\2E\u0103\3\2\2\2G\u0105\3\2\2\2I\u0107\3\2\2\2")
        buf.write("K\u010a\3\2\2\2M\u010d\3\2\2\2O\u010f\3\2\2\2Q\u0112\3")
        buf.write("\2\2\2S\u0114\3\2\2\2U\u0116\3\2\2\2W\u0118\3\2\2\2Y\u011a")
        buf.write("\3\2\2\2[\u011c\3\2\2\2]\u011e\3\2\2\2_\u0120\3\2\2\2")
        buf.write("a\u0123\3\2\2\2c\u0129\3\2\2\2e\u012b\3\2\2\2g\u012d\3")
        buf.write("\2\2\2ij\7o\2\2jk\7c\2\2kl\7k\2\2lm\7p\2\2m\4\3\2\2\2")
        buf.write("no\7k\2\2op\7p\2\2pq\7v\2\2q\6\3\2\2\2rs\7x\2\2st\7q\2")
        buf.write("\2tu\7k\2\2uv\7f\2\2v\b\3\2\2\2wx\7d\2\2xy\7t\2\2yz\7")
        buf.write("g\2\2z{\7c\2\2{|\7m\2\2|}\3\2\2\2}~\5]/\2~\n\3\2\2\2\177")
        buf.write("\u0080\7e\2\2\u0080\u0081\7q\2\2\u0081\u0082\7p\2\2\u0082")
        buf.write("\u0083\7v\2\2\u0083\u0084\7k\2\2\u0084\u0085\7p\2\2\u0085")
        buf.write("\u0086\7w\2\2\u0086\u0087\7g\2\2\u0087\u0088\3\2\2\2\u0088")
        buf.write("\u0089\5]/\2\u0089\f\3\2\2\2\u008a\u008b\7h\2\2\u008b")
        buf.write("\u008c\7q\2\2\u008c\u008d\7t\2\2\u008d\16\3\2\2\2\u008e")
        buf.write("\u008f\7k\2\2\u008f\u0090\7h\2\2\u0090\20\3\2\2\2\u0091")
        buf.write("\u0092\7v\2\2\u0092\u0093\7j\2\2\u0093\u0094\7g\2\2\u0094")
        buf.write("\u0095\7p\2\2\u0095\22\3\2\2\2\u0096\u0097\7g\2\2\u0097")
        buf.write("\u0098\7n\2\2\u0098\u0099\7u\2\2\u0099\u009a\7g\2\2\u009a")
        buf.write("\24\3\2\2\2\u009b\u009c\7t\2\2\u009c\u009d\7g\2\2\u009d")
        buf.write("\u009e\7v\2\2\u009e\u009f\7w\2\2\u009f\u00a0\7t\2\2\u00a0")
        buf.write("\u00a1\7p\2\2\u00a1\26\3\2\2\2\u00a2\u00a3\7y\2\2\u00a3")
        buf.write("\u00a4\7j\2\2\u00a4\u00a5\7k\2\2\u00a5\u00a6\7n\2\2\u00a6")
        buf.write("\u00a7\7g\2\2\u00a7\30\3\2\2\2\u00a8\u00a9\7d\2\2\u00a9")
        buf.write("\u00aa\7q\2\2\u00aa\u00ab\7q\2\2\u00ab\u00ac\7n\2\2\u00ac")
        buf.write("\u00ad\7g\2\2\u00ad\u00ae\7c\2\2\u00ae\u00af\7p\2\2\u00af")
        buf.write("\32\3\2\2\2\u00b0\u00b1\5\7\4\2\u00b1\34\3\2\2\2\u00b2")
        buf.write("\u00b3\7f\2\2\u00b3\u00b4\7q\2\2\u00b4\36\3\2\2\2\u00b5")
        buf.write("\u00b6\7v\2\2\u00b6\u00b7\7t\2\2\u00b7\u00b8\7w\2\2\u00b8")
        buf.write("\u00b9\7g\2\2\u00b9 \3\2\2\2\u00ba\u00bb\7h\2\2\u00bb")
        buf.write("\u00bc\7c\2\2\u00bc\u00bd\7n\2\2\u00bd\u00be\7u\2\2\u00be")
        buf.write("\u00bf\7g\2\2\u00bf\"\3\2\2\2\u00c0\u00c4\5%\23\2\u00c1")
        buf.write("\u00c3\5\'\24\2\u00c2\u00c1\3\2\2\2\u00c3\u00c6\3\2\2")
        buf.write("\2\u00c4\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5$\3\2")
        buf.write("\2\2\u00c6\u00c4\3\2\2\2\u00c7\u00c8\t\2\2\2\u00c8&\3")
        buf.write("\2\2\2\u00c9\u00ca\t\3\2\2\u00ca(\3\2\2\2\u00cb\u00cd")
        buf.write("\t\4\2\2\u00cc\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce")
        buf.write("\u00cc\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf*\3\2\2\2\u00d0")
        buf.write("\u00d2\5-\27\2\u00d1\u00d3\5/\30\2\u00d2\u00d1\3\2\2\2")
        buf.write("\u00d2\u00d3\3\2\2\2\u00d3\u00d8\3\2\2\2\u00d4\u00d5\5")
        buf.write(")\25\2\u00d5\u00d6\5/\30\2\u00d6\u00d8\3\2\2\2\u00d7\u00d0")
        buf.write("\3\2\2\2\u00d7\u00d4\3\2\2\2\u00d8,\3\2\2\2\u00d9\u00da")
        buf.write("\5)\25\2\u00da\u00db\7\60\2\2\u00db\u00e3\3\2\2\2\u00dc")
        buf.write("\u00dd\7\60\2\2\u00dd\u00e3\5)\25\2\u00de\u00df\5)\25")
        buf.write("\2\u00df\u00e0\7\60\2\2\u00e0\u00e1\5)\25\2\u00e1\u00e3")
        buf.write("\3\2\2\2\u00e2\u00d9\3\2\2\2\u00e2\u00dc\3\2\2\2\u00e2")
        buf.write("\u00de\3\2\2\2\u00e3.\3\2\2\2\u00e4\u00e6\t\5\2\2\u00e5")
        buf.write("\u00e7\5C\"\2\u00e6\u00e5\3\2\2\2\u00e6\u00e7\3\2\2\2")
        buf.write("\u00e7\u00e8\3\2\2\2\u00e8\u00e9\5)\25\2\u00e9\60\3\2")
        buf.write("\2\2\u00ea\u00ed\5\37\20\2\u00eb\u00ed\5!\21\2\u00ec\u00ea")
        buf.write("\3\2\2\2\u00ec\u00eb\3\2\2\2\u00ed\62\3\2\2\2\u00ee\u00ef")
        buf.write("\7-\2\2\u00ef\64\3\2\2\2\u00f0\u00f1\7,\2\2\u00f1\66\3")
        buf.write("\2\2\2\u00f2\u00f3\7#\2\2\u00f38\3\2\2\2\u00f4\u00f5\7")
        buf.write("~\2\2\u00f5\u00f6\7~\2\2\u00f6:\3\2\2\2\u00f7\u00f8\7")
        buf.write("#\2\2\u00f8\u00f9\7?\2\2\u00f9<\3\2\2\2\u00fa\u00fb\7")
        buf.write(">\2\2\u00fb>\3\2\2\2\u00fc\u00fd\7>\2\2\u00fd\u00fe\7")
        buf.write("?\2\2\u00fe@\3\2\2\2\u00ff\u0100\7?\2\2\u0100B\3\2\2\2")
        buf.write("\u0101\u0102\7/\2\2\u0102D\3\2\2\2\u0103\u0104\7\61\2")
        buf.write("\2\u0104F\3\2\2\2\u0105\u0106\7\'\2\2\u0106H\3\2\2\2\u0107")
        buf.write("\u0108\7(\2\2\u0108\u0109\7(\2\2\u0109J\3\2\2\2\u010a")
        buf.write("\u010b\7?\2\2\u010b\u010c\7?\2\2\u010cL\3\2\2\2\u010d")
        buf.write("\u010e\7@\2\2\u010eN\3\2\2\2\u010f\u0110\7@\2\2\u0110")
        buf.write("\u0111\7?\2\2\u0111P\3\2\2\2\u0112\u0113\7]\2\2\u0113")
        buf.write("R\3\2\2\2\u0114\u0115\7_\2\2\u0115T\3\2\2\2\u0116\u0117")
        buf.write("\7*\2\2\u0117V\3\2\2\2\u0118\u0119\7+\2\2\u0119X\3\2\2")
        buf.write("\2\u011a\u011b\7}\2\2\u011bZ\3\2\2\2\u011c\u011d\7\177")
        buf.write("\2\2\u011d\\\3\2\2\2\u011e\u011f\7=\2\2\u011f^\3\2\2\2")
        buf.write("\u0120\u0121\7.\2\2\u0121`\3\2\2\2\u0122\u0124\t\6\2\2")
        buf.write("\u0123\u0122\3\2\2\2\u0124\u0125\3\2\2\2\u0125\u0123\3")
        buf.write("\2\2\2\u0125\u0126\3\2\2\2\u0126\u0127\3\2\2\2\u0127\u0128")
        buf.write("\b\61\2\2\u0128b\3\2\2\2\u0129\u012a\13\2\2\2\u012ad\3")
        buf.write("\2\2\2\u012b\u012c\13\2\2\2\u012cf\3\2\2\2\u012d\u012e")
        buf.write("\13\2\2\2\u012eh\3\2\2\2\13\2\u00c4\u00ce\u00d2\u00d7")
        buf.write("\u00e2\u00e6\u00ec\u0125\3\b\2\2")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    INTTYPE = 2
    VOIDTYPE = 3
    BREAKSt = 4
    CONTINUESt = 5
    FOR = 6
    IF = 7
    THEN = 8
    ELSE = 9
    RETURN = 10
    WHILE = 11
    BOOLEAN = 12
    VOID = 13
    DO = 14
    TRUE = 15
    FALSE = 16
    ID = 17
    INTLIT = 18
    FLOATLIT = 19
    BOOLIT = 20
    ADD = 21
    MUL = 22
    LOGN = 23
    LOGO = 24
    NOTE = 25
    LT = 26
    LTOE = 27
    ASSIG = 28
    SUB = 29
    DIV = 30
    MOD = 31
    LOGA = 32
    EQ = 33
    GT = 34
    GTOE = 35
    LSB = 36
    RSB = 37
    LB = 38
    RB = 39
    LP = 40
    RP = 41
    SEMI = 42
    CM = 43
    WS = 44
    ERROR_CHAR = 45
    UNCLOSE_STRING = 46
    ILLEGAL_ESCAPE = 47

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'int'", "'void'", "'for'", "'if'", "'then'", "'else'", 
            "'return'", "'while'", "'boolean'", "'do'", "'true'", "'false'", 
            "'+'", "'*'", "'!'", "'||'", "'!='", "'<'", "'<='", "'='", "'-'", 
            "'/'", "'%'", "'&&'", "'=='", "'>'", "'>='", "'['", "']'", "'('", 
            "')'", "'{'", "'}'", "';'", "','" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "VOIDTYPE", "BREAKSt", "CONTINUESt", "FOR", "IF", 
            "THEN", "ELSE", "RETURN", "WHILE", "BOOLEAN", "VOID", "DO", 
            "TRUE", "FALSE", "ID", "INTLIT", "FLOATLIT", "BOOLIT", "ADD", 
            "MUL", "LOGN", "LOGO", "NOTE", "LT", "LTOE", "ASSIG", "SUB", 
            "DIV", "MOD", "LOGA", "EQ", "GT", "GTOE", "LSB", "RSB", "LB", 
            "RB", "LP", "RP", "SEMI", "CM", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "INTTYPE", "VOIDTYPE", "BREAKSt", "CONTINUESt", 
                  "FOR", "IF", "THEN", "ELSE", "RETURN", "WHILE", "BOOLEAN", 
                  "VOID", "DO", "TRUE", "FALSE", "ID", "Letter", "LetterOrDigit", 
                  "INTLIT", "FLOATLIT", "NUMPART", "DECPART", "BOOLIT", 
                  "ADD", "MUL", "LOGN", "LOGO", "NOTE", "LT", "LTOE", "ASSIG", 
                  "SUB", "DIV", "MOD", "LOGA", "EQ", "GT", "GTOE", "LSB", 
                  "RSB", "LB", "RB", "LP", "RP", "SEMI", "CM", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


