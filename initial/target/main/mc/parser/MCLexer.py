# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\61")
        buf.write("\u0125\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\6\22\u00be\n")
        buf.write("\22\r\22\16\22\u00bf\3\23\6\23\u00c3\n\23\r\23\16\23\u00c4")
        buf.write("\3\24\3\24\5\24\u00c9\n\24\3\24\3\24\3\24\5\24\u00ce\n")
        buf.write("\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25")
        buf.write("\u00d9\n\25\3\26\3\26\5\26\u00dd\n\26\3\26\3\26\3\27\3")
        buf.write("\27\5\27\u00e3\n\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3&\3")
        buf.write("&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3")
        buf.write(".\3/\6/\u011a\n/\r/\16/\u011b\3/\3/\3\60\3\60\3\61\3\61")
        buf.write("\3\62\3\62\2\2\63\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\2+\2-\26/\27\61\30\63\31\65\32\67\339\34;\35=\36?\37")
        buf.write("A C!E\"G#I$K%M&O\'Q(S)U*W+Y,[-]._/a\60c\61\3\2\6\4\2C")
        buf.write("\\c|\3\2\62;\4\2GGgg\5\2\13\f\17\17\"\"\2\u012b\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2")
        buf.write("\2\2\2\'\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2")
        buf.write("\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3")
        buf.write("\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E")
        buf.write("\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2")
        buf.write("O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2")
        buf.write("\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2")
        buf.write("\2\2c\3\2\2\2\3e\3\2\2\2\5j\3\2\2\2\7n\3\2\2\2\ts\3\2")
        buf.write("\2\2\13{\3\2\2\2\r\u0086\3\2\2\2\17\u008a\3\2\2\2\21\u008d")
        buf.write("\3\2\2\2\23\u0092\3\2\2\2\25\u0097\3\2\2\2\27\u009e\3")
        buf.write("\2\2\2\31\u00a4\3\2\2\2\33\u00ac\3\2\2\2\35\u00ae\3\2")
        buf.write("\2\2\37\u00b1\3\2\2\2!\u00b6\3\2\2\2#\u00bd\3\2\2\2%\u00c2")
        buf.write("\3\2\2\2\'\u00cd\3\2\2\2)\u00d8\3\2\2\2+\u00da\3\2\2\2")
        buf.write("-\u00e2\3\2\2\2/\u00e4\3\2\2\2\61\u00e6\3\2\2\2\63\u00e8")
        buf.write("\3\2\2\2\65\u00ea\3\2\2\2\67\u00ed\3\2\2\29\u00f0\3\2")
        buf.write("\2\2;\u00f2\3\2\2\2=\u00f5\3\2\2\2?\u00f7\3\2\2\2A\u00f9")
        buf.write("\3\2\2\2C\u00fb\3\2\2\2E\u00fd\3\2\2\2G\u0100\3\2\2\2")
        buf.write("I\u0103\3\2\2\2K\u0105\3\2\2\2M\u0108\3\2\2\2O\u010a\3")
        buf.write("\2\2\2Q\u010c\3\2\2\2S\u010e\3\2\2\2U\u0110\3\2\2\2W\u0112")
        buf.write("\3\2\2\2Y\u0114\3\2\2\2[\u0116\3\2\2\2]\u0119\3\2\2\2")
        buf.write("_\u011f\3\2\2\2a\u0121\3\2\2\2c\u0123\3\2\2\2ef\7o\2\2")
        buf.write("fg\7c\2\2gh\7k\2\2hi\7p\2\2i\4\3\2\2\2jk\7k\2\2kl\7p\2")
        buf.write("\2lm\7v\2\2m\6\3\2\2\2no\7x\2\2op\7q\2\2pq\7k\2\2qr\7")
        buf.write("f\2\2r\b\3\2\2\2st\7d\2\2tu\7t\2\2uv\7g\2\2vw\7c\2\2w")
        buf.write("x\7m\2\2xy\3\2\2\2yz\5Y-\2z\n\3\2\2\2{|\7e\2\2|}\7q\2")
        buf.write("\2}~\7p\2\2~\177\7v\2\2\177\u0080\7k\2\2\u0080\u0081\7")
        buf.write("p\2\2\u0081\u0082\7w\2\2\u0082\u0083\7g\2\2\u0083\u0084")
        buf.write("\3\2\2\2\u0084\u0085\5Y-\2\u0085\f\3\2\2\2\u0086\u0087")
        buf.write("\7h\2\2\u0087\u0088\7q\2\2\u0088\u0089\7t\2\2\u0089\16")
        buf.write("\3\2\2\2\u008a\u008b\7k\2\2\u008b\u008c\7h\2\2\u008c\20")
        buf.write("\3\2\2\2\u008d\u008e\7v\2\2\u008e\u008f\7j\2\2\u008f\u0090")
        buf.write("\7g\2\2\u0090\u0091\7p\2\2\u0091\22\3\2\2\2\u0092\u0093")
        buf.write("\7g\2\2\u0093\u0094\7n\2\2\u0094\u0095\7u\2\2\u0095\u0096")
        buf.write("\7g\2\2\u0096\24\3\2\2\2\u0097\u0098\7t\2\2\u0098\u0099")
        buf.write("\7g\2\2\u0099\u009a\7v\2\2\u009a\u009b\7w\2\2\u009b\u009c")
        buf.write("\7t\2\2\u009c\u009d\7p\2\2\u009d\26\3\2\2\2\u009e\u009f")
        buf.write("\7y\2\2\u009f\u00a0\7j\2\2\u00a0\u00a1\7k\2\2\u00a1\u00a2")
        buf.write("\7n\2\2\u00a2\u00a3\7g\2\2\u00a3\30\3\2\2\2\u00a4\u00a5")
        buf.write("\7d\2\2\u00a5\u00a6\7q\2\2\u00a6\u00a7\7q\2\2\u00a7\u00a8")
        buf.write("\7n\2\2\u00a8\u00a9\7g\2\2\u00a9\u00aa\7c\2\2\u00aa\u00ab")
        buf.write("\7p\2\2\u00ab\32\3\2\2\2\u00ac\u00ad\5\7\4\2\u00ad\34")
        buf.write("\3\2\2\2\u00ae\u00af\7f\2\2\u00af\u00b0\7q\2\2\u00b0\36")
        buf.write("\3\2\2\2\u00b1\u00b2\7v\2\2\u00b2\u00b3\7t\2\2\u00b3\u00b4")
        buf.write("\7w\2\2\u00b4\u00b5\7g\2\2\u00b5 \3\2\2\2\u00b6\u00b7")
        buf.write("\7h\2\2\u00b7\u00b8\7c\2\2\u00b8\u00b9\7n\2\2\u00b9\u00ba")
        buf.write("\7u\2\2\u00ba\u00bb\7g\2\2\u00bb\"\3\2\2\2\u00bc\u00be")
        buf.write("\t\2\2\2\u00bd\u00bc\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf")
        buf.write("\u00bd\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0$\3\2\2\2\u00c1")
        buf.write("\u00c3\t\3\2\2\u00c2\u00c1\3\2\2\2\u00c3\u00c4\3\2\2\2")
        buf.write("\u00c4\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5&\3\2\2")
        buf.write("\2\u00c6\u00c8\5)\25\2\u00c7\u00c9\5+\26\2\u00c8\u00c7")
        buf.write("\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\u00ce\3\2\2\2\u00ca")
        buf.write("\u00cb\5%\23\2\u00cb\u00cc\5+\26\2\u00cc\u00ce\3\2\2\2")
        buf.write("\u00cd\u00c6\3\2\2\2\u00cd\u00ca\3\2\2\2\u00ce(\3\2\2")
        buf.write("\2\u00cf\u00d0\5%\23\2\u00d0\u00d1\7\60\2\2\u00d1\u00d9")
        buf.write("\3\2\2\2\u00d2\u00d3\7\60\2\2\u00d3\u00d9\5%\23\2\u00d4")
        buf.write("\u00d5\5%\23\2\u00d5\u00d6\7\60\2\2\u00d6\u00d7\5%\23")
        buf.write("\2\u00d7\u00d9\3\2\2\2\u00d8\u00cf\3\2\2\2\u00d8\u00d2")
        buf.write("\3\2\2\2\u00d8\u00d4\3\2\2\2\u00d9*\3\2\2\2\u00da\u00dc")
        buf.write("\t\4\2\2\u00db\u00dd\5? \2\u00dc\u00db\3\2\2\2\u00dc\u00dd")
        buf.write("\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00df\5%\23\2\u00df")
        buf.write(",\3\2\2\2\u00e0\u00e3\5\37\20\2\u00e1\u00e3\5!\21\2\u00e2")
        buf.write("\u00e0\3\2\2\2\u00e2\u00e1\3\2\2\2\u00e3.\3\2\2\2\u00e4")
        buf.write("\u00e5\7-\2\2\u00e5\60\3\2\2\2\u00e6\u00e7\7,\2\2\u00e7")
        buf.write("\62\3\2\2\2\u00e8\u00e9\7#\2\2\u00e9\64\3\2\2\2\u00ea")
        buf.write("\u00eb\7~\2\2\u00eb\u00ec\7~\2\2\u00ec\66\3\2\2\2\u00ed")
        buf.write("\u00ee\7#\2\2\u00ee\u00ef\7?\2\2\u00ef8\3\2\2\2\u00f0")
        buf.write("\u00f1\7>\2\2\u00f1:\3\2\2\2\u00f2\u00f3\7>\2\2\u00f3")
        buf.write("\u00f4\7?\2\2\u00f4<\3\2\2\2\u00f5\u00f6\7?\2\2\u00f6")
        buf.write(">\3\2\2\2\u00f7\u00f8\7/\2\2\u00f8@\3\2\2\2\u00f9\u00fa")
        buf.write("\7\61\2\2\u00faB\3\2\2\2\u00fb\u00fc\7\'\2\2\u00fcD\3")
        buf.write("\2\2\2\u00fd\u00fe\7(\2\2\u00fe\u00ff\7(\2\2\u00ffF\3")
        buf.write("\2\2\2\u0100\u0101\7?\2\2\u0101\u0102\7?\2\2\u0102H\3")
        buf.write("\2\2\2\u0103\u0104\7@\2\2\u0104J\3\2\2\2\u0105\u0106\7")
        buf.write("@\2\2\u0106\u0107\7?\2\2\u0107L\3\2\2\2\u0108\u0109\7")
        buf.write("]\2\2\u0109N\3\2\2\2\u010a\u010b\7_\2\2\u010bP\3\2\2\2")
        buf.write("\u010c\u010d\7*\2\2\u010dR\3\2\2\2\u010e\u010f\7+\2\2")
        buf.write("\u010fT\3\2\2\2\u0110\u0111\7}\2\2\u0111V\3\2\2\2\u0112")
        buf.write("\u0113\7\177\2\2\u0113X\3\2\2\2\u0114\u0115\7=\2\2\u0115")
        buf.write("Z\3\2\2\2\u0116\u0117\7.\2\2\u0117\\\3\2\2\2\u0118\u011a")
        buf.write("\t\5\2\2\u0119\u0118\3\2\2\2\u011a\u011b\3\2\2\2\u011b")
        buf.write("\u0119\3\2\2\2\u011b\u011c\3\2\2\2\u011c\u011d\3\2\2\2")
        buf.write("\u011d\u011e\b/\2\2\u011e^\3\2\2\2\u011f\u0120\13\2\2")
        buf.write("\2\u0120`\3\2\2\2\u0121\u0122\13\2\2\2\u0122b\3\2\2\2")
        buf.write("\u0123\u0124\13\2\2\2\u0124d\3\2\2\2\13\2\u00bf\u00c4")
        buf.write("\u00c8\u00cd\u00d8\u00dc\u00e2\u011b\3\b\2\2")
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
                  "VOID", "DO", "TRUE", "FALSE", "ID", "INTLIT", "FLOATLIT", 
                  "NUMPART", "DECPART", "BOOLIT", "ADD", "MUL", "LOGN", 
                  "LOGO", "NOTE", "LT", "LTOE", "ASSIG", "SUB", "DIV", "MOD", 
                  "LOGA", "EQ", "GT", "GTOE", "LSB", "RSB", "LB", "RB", 
                  "LP", "RP", "SEMI", "CM", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


