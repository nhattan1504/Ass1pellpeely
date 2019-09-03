# Generated from /home/ktant/Documents/PPL/assignment1/initial/src/main/mc/parser/MC.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2,")
        buf.write("\u010a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\6\r\u009c")
        buf.write("\n\r\r\r\16\r\u009d\3\16\6\16\u00a1\n\16\r\16\16\16\u00a2")
        buf.write("\3\17\3\17\5\17\u00a7\n\17\3\17\3\17\3\17\5\17\u00ac\n")
        buf.write("\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20")
        buf.write("\u00b7\n\20\3\21\3\21\5\21\u00bb\n\21\3\21\3\21\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u00c8\n\22")
        buf.write("\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\33\3\33\3\34")
        buf.write("\3\34\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3")
        buf.write("!\3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(")
        buf.write("\3)\3)\3*\6*\u00ff\n*\r*\16*\u0100\3*\3*\3+\3+\3,\3,\3")
        buf.write("-\3-\2\2.\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\2!\2#\21%\22\'\23)\24+\25")
        buf.write("-\26/\27\61\30\63\31\65\32\67\339\34;\35=\36?\37A C!E")
        buf.write("\"G#I$K%M&O\'Q(S)U*W+Y,\3\2\6\4\2C\\c|\3\2\62;\4\2GGg")
        buf.write("g\5\2\13\f\17\17\"\"\2\u0110\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2#\3\2\2\2")
        buf.write("\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2")
        buf.write("\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2")
        buf.write("\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2")
        buf.write("\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2")
        buf.write("\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3")
        buf.write("\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\3[\3\2\2\2\5`")
        buf.write("\3\2\2\2\7d\3\2\2\2\ti\3\2\2\2\13q\3\2\2\2\r|\3\2\2\2")
        buf.write("\17\u0080\3\2\2\2\21\u0083\3\2\2\2\23\u0088\3\2\2\2\25")
        buf.write("\u008d\3\2\2\2\27\u0094\3\2\2\2\31\u009b\3\2\2\2\33\u00a0")
        buf.write("\3\2\2\2\35\u00ab\3\2\2\2\37\u00b6\3\2\2\2!\u00b8\3\2")
        buf.write("\2\2#\u00c7\3\2\2\2%\u00c9\3\2\2\2\'\u00cb\3\2\2\2)\u00cd")
        buf.write("\3\2\2\2+\u00cf\3\2\2\2-\u00d2\3\2\2\2/\u00d5\3\2\2\2")
        buf.write("\61\u00d7\3\2\2\2\63\u00da\3\2\2\2\65\u00dc\3\2\2\2\67")
        buf.write("\u00de\3\2\2\29\u00e0\3\2\2\2;\u00e2\3\2\2\2=\u00e5\3")
        buf.write("\2\2\2?\u00e8\3\2\2\2A\u00ea\3\2\2\2C\u00ed\3\2\2\2E\u00ef")
        buf.write("\3\2\2\2G\u00f1\3\2\2\2I\u00f3\3\2\2\2K\u00f5\3\2\2\2")
        buf.write("M\u00f7\3\2\2\2O\u00f9\3\2\2\2Q\u00fb\3\2\2\2S\u00fe\3")
        buf.write("\2\2\2U\u0104\3\2\2\2W\u0106\3\2\2\2Y\u0108\3\2\2\2[\\")
        buf.write("\7o\2\2\\]\7c\2\2]^\7k\2\2^_\7p\2\2_\4\3\2\2\2`a\7k\2")
        buf.write("\2ab\7p\2\2bc\7v\2\2c\6\3\2\2\2de\7x\2\2ef\7q\2\2fg\7")
        buf.write("k\2\2gh\7f\2\2h\b\3\2\2\2ij\7d\2\2jk\7t\2\2kl\7g\2\2l")
        buf.write("m\7c\2\2mn\7m\2\2no\3\2\2\2op\5O(\2p\n\3\2\2\2qr\7e\2")
        buf.write("\2rs\7q\2\2st\7p\2\2tu\7v\2\2uv\7k\2\2vw\7p\2\2wx\7w\2")
        buf.write("\2xy\7g\2\2yz\3\2\2\2z{\5O(\2{\f\3\2\2\2|}\7h\2\2}~\7")
        buf.write("q\2\2~\177\7t\2\2\177\16\3\2\2\2\u0080\u0081\7k\2\2\u0081")
        buf.write("\u0082\7h\2\2\u0082\20\3\2\2\2\u0083\u0084\7v\2\2\u0084")
        buf.write("\u0085\7j\2\2\u0085\u0086\7g\2\2\u0086\u0087\7p\2\2\u0087")
        buf.write("\22\3\2\2\2\u0088\u0089\7g\2\2\u0089\u008a\7n\2\2\u008a")
        buf.write("\u008b\7u\2\2\u008b\u008c\7g\2\2\u008c\24\3\2\2\2\u008d")
        buf.write("\u008e\7t\2\2\u008e\u008f\7g\2\2\u008f\u0090\7v\2\2\u0090")
        buf.write("\u0091\7w\2\2\u0091\u0092\7t\2\2\u0092\u0093\7p\2\2\u0093")
        buf.write("\26\3\2\2\2\u0094\u0095\7y\2\2\u0095\u0096\7j\2\2\u0096")
        buf.write("\u0097\7k\2\2\u0097\u0098\7n\2\2\u0098\u0099\7g\2\2\u0099")
        buf.write("\30\3\2\2\2\u009a\u009c\t\2\2\2\u009b\u009a\3\2\2\2\u009c")
        buf.write("\u009d\3\2\2\2\u009d\u009b\3\2\2\2\u009d\u009e\3\2\2\2")
        buf.write("\u009e\32\3\2\2\2\u009f\u00a1\t\3\2\2\u00a0\u009f\3\2")
        buf.write("\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2\u00a3")
        buf.write("\3\2\2\2\u00a3\34\3\2\2\2\u00a4\u00a6\5\37\20\2\u00a5")
        buf.write("\u00a7\5!\21\2\u00a6\u00a5\3\2\2\2\u00a6\u00a7\3\2\2\2")
        buf.write("\u00a7\u00ac\3\2\2\2\u00a8\u00a9\5\33\16\2\u00a9\u00aa")
        buf.write("\5!\21\2\u00aa\u00ac\3\2\2\2\u00ab\u00a4\3\2\2\2\u00ab")
        buf.write("\u00a8\3\2\2\2\u00ac\36\3\2\2\2\u00ad\u00ae\5\33\16\2")
        buf.write("\u00ae\u00af\7\60\2\2\u00af\u00b7\3\2\2\2\u00b0\u00b1")
        buf.write("\7\60\2\2\u00b1\u00b7\5\33\16\2\u00b2\u00b3\5\33\16\2")
        buf.write("\u00b3\u00b4\7\60\2\2\u00b4\u00b5\5\33\16\2\u00b5\u00b7")
        buf.write("\3\2\2\2\u00b6\u00ad\3\2\2\2\u00b6\u00b0\3\2\2\2\u00b6")
        buf.write("\u00b2\3\2\2\2\u00b7 \3\2\2\2\u00b8\u00ba\t\4\2\2\u00b9")
        buf.write("\u00bb\5\65\33\2\u00ba\u00b9\3\2\2\2\u00ba\u00bb\3\2\2")
        buf.write("\2\u00bb\u00bc\3\2\2\2\u00bc\u00bd\5\33\16\2\u00bd\"\3")
        buf.write("\2\2\2\u00be\u00bf\7v\2\2\u00bf\u00c0\7t\2\2\u00c0\u00c1")
        buf.write("\7w\2\2\u00c1\u00c8\7g\2\2\u00c2\u00c3\7h\2\2\u00c3\u00c4")
        buf.write("\7c\2\2\u00c4\u00c5\7n\2\2\u00c5\u00c6\7u\2\2\u00c6\u00c8")
        buf.write("\7g\2\2\u00c7\u00be\3\2\2\2\u00c7\u00c2\3\2\2\2\u00c8")
        buf.write("$\3\2\2\2\u00c9\u00ca\7-\2\2\u00ca&\3\2\2\2\u00cb\u00cc")
        buf.write("\7,\2\2\u00cc(\3\2\2\2\u00cd\u00ce\7#\2\2\u00ce*\3\2\2")
        buf.write("\2\u00cf\u00d0\7~\2\2\u00d0\u00d1\7~\2\2\u00d1,\3\2\2")
        buf.write("\2\u00d2\u00d3\7#\2\2\u00d3\u00d4\7?\2\2\u00d4.\3\2\2")
        buf.write("\2\u00d5\u00d6\7>\2\2\u00d6\60\3\2\2\2\u00d7\u00d8\7>")
        buf.write("\2\2\u00d8\u00d9\7?\2\2\u00d9\62\3\2\2\2\u00da\u00db\7")
        buf.write("?\2\2\u00db\64\3\2\2\2\u00dc\u00dd\7/\2\2\u00dd\66\3\2")
        buf.write("\2\2\u00de\u00df\7\61\2\2\u00df8\3\2\2\2\u00e0\u00e1\7")
        buf.write("\'\2\2\u00e1:\3\2\2\2\u00e2\u00e3\7(\2\2\u00e3\u00e4\7")
        buf.write("(\2\2\u00e4<\3\2\2\2\u00e5\u00e6\7?\2\2\u00e6\u00e7\7")
        buf.write("?\2\2\u00e7>\3\2\2\2\u00e8\u00e9\7@\2\2\u00e9@\3\2\2\2")
        buf.write("\u00ea\u00eb\7@\2\2\u00eb\u00ec\7?\2\2\u00ecB\3\2\2\2")
        buf.write("\u00ed\u00ee\7]\2\2\u00eeD\3\2\2\2\u00ef\u00f0\7_\2\2")
        buf.write("\u00f0F\3\2\2\2\u00f1\u00f2\7*\2\2\u00f2H\3\2\2\2\u00f3")
        buf.write("\u00f4\7+\2\2\u00f4J\3\2\2\2\u00f5\u00f6\7}\2\2\u00f6")
        buf.write("L\3\2\2\2\u00f7\u00f8\7\177\2\2\u00f8N\3\2\2\2\u00f9\u00fa")
        buf.write("\7=\2\2\u00faP\3\2\2\2\u00fb\u00fc\7.\2\2\u00fcR\3\2\2")
        buf.write("\2\u00fd\u00ff\t\5\2\2\u00fe\u00fd\3\2\2\2\u00ff\u0100")
        buf.write("\3\2\2\2\u0100\u00fe\3\2\2\2\u0100\u0101\3\2\2\2\u0101")
        buf.write("\u0102\3\2\2\2\u0102\u0103\b*\2\2\u0103T\3\2\2\2\u0104")
        buf.write("\u0105\13\2\2\2\u0105V\3\2\2\2\u0106\u0107\13\2\2\2\u0107")
        buf.write("X\3\2\2\2\u0108\u0109\13\2\2\2\u0109Z\3\2\2\2\13\2\u009d")
        buf.write("\u00a2\u00a6\u00ab\u00b6\u00ba\u00c7\u0100\3\b\2\2")
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
    ID = 12
    INTLIT = 13
    FLOATLIT = 14
    BOOLIT = 15
    ADD = 16
    MUL = 17
    LOGN = 18
    LOGO = 19
    NOTE = 20
    LT = 21
    LTOE = 22
    ASSIG = 23
    SUB = 24
    DIV = 25
    MOD = 26
    LOGA = 27
    EQ = 28
    GT = 29
    GTOE = 30
    LSB = 31
    RSB = 32
    LB = 33
    RB = 34
    LP = 35
    RP = 36
    SEMI = 37
    CM = 38
    WS = 39
    ERROR_CHAR = 40
    UNCLOSE_STRING = 41
    ILLEGAL_ESCAPE = 42

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'int'", "'void'", "'for'", "'if'", "'then'", "'else'", 
            "'return'", "'while'", "'+'", "'*'", "'!'", "'||'", "'!='", 
            "'<'", "'<='", "'='", "'-'", "'/'", "'%'", "'&&'", "'=='", "'>'", 
            "'>='", "'['", "']'", "'('", "')'", "'{'", "'}'", "';'", "','" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "VOIDTYPE", "BREAKSt", "CONTINUESt", "FOR", "IF", 
            "THEN", "ELSE", "RETURN", "WHILE", "ID", "INTLIT", "FLOATLIT", 
            "BOOLIT", "ADD", "MUL", "LOGN", "LOGO", "NOTE", "LT", "LTOE", 
            "ASSIG", "SUB", "DIV", "MOD", "LOGA", "EQ", "GT", "GTOE", "LSB", 
            "RSB", "LB", "RB", "LP", "RP", "SEMI", "CM", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "INTTYPE", "VOIDTYPE", "BREAKSt", "CONTINUESt", 
                  "FOR", "IF", "THEN", "ELSE", "RETURN", "WHILE", "ID", 
                  "INTLIT", "FLOATLIT", "NUMPART", "DECPART", "BOOLIT", 
                  "ADD", "MUL", "LOGN", "LOGO", "NOTE", "LT", "LTOE", "ASSIG", 
                  "SUB", "DIV", "MOD", "LOGA", "EQ", "GT", "GTOE", "LSB", 
                  "RSB", "LB", "RB", "LP", "RP", "SEMI", "CM", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


