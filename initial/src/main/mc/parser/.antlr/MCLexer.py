# Generated from /home/ktant/Documents/PPL/assignment1/initial/src/main/mc/parser/MC.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2?")
        buf.write("\u01ac\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\3\2\3")
        buf.write("\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\5\6\u0093")
        buf.write("\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u009d\n\7\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\5\20\u00da\n\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\5\21\u00e4\n\21")
        buf.write("\3\22\3\22\3\22\5\22\u00e9\n\22\3\22\3\22\3\22\3\22\3")
        buf.write("\23\3\23\3\23\5\23\u00f2\n\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\36\3\36\7\36\u0127\n\36\f\36\16\36\u012a\13\36\3\37")
        buf.write("\3\37\3 \3 \3!\6!\u0131\n!\r!\16!\u0132\3\"\3\"\5\"\u0137")
        buf.write("\n\"\3\"\3\"\3\"\5\"\u013c\n\"\3#\3#\3#\3#\3#\3#\3#\3")
        buf.write("#\3#\5#\u0147\n#\3$\3$\5$\u014b\n$\3$\3$\3%\3%\5%\u0151")
        buf.write("\n%\3&\3&\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3,\3,")
        buf.write("\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\61\3\62\3")
        buf.write("\62\3\62\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\66\3\66")
        buf.write("\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\6=\u0188\n")
        buf.write("=\r=\16=\u0189\3=\3=\3>\3>\3>\3>\7>\u0192\n>\f>\16>\u0195")
        buf.write("\13>\3>\3>\3>\3>\3>\3?\3?\3?\3?\7?\u01a0\n?\f?\16?\u01a3")
        buf.write("\13?\3?\3?\3@\3@\3A\3A\3B\3B\4\u0193\u01a1\2C\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37=\2?\2A C!E\2G\2I\"K#M$O%Q&S\'")
        buf.write("U(W)Y*[+],_-a.c/e\60g\61i\62k\63m\64o\65q\66s\67u8w9y")
        buf.write(":{;}<\177=\u0081>\u0083?\3\2\7\5\2C\\aac|\6\2\62;C\\a")
        buf.write("ac|\3\2\62;\4\2GGgg\5\2\13\f\17\17\"\"\2\u01be\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2I\3\2\2")
        buf.write("\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2")
        buf.write("\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3")
        buf.write("\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g")
        buf.write("\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2")
        buf.write("q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2")
        buf.write("\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2")
        buf.write("\u0083\3\2\2\2\3\u0085\3\2\2\2\5\u0087\3\2\2\2\7\u0089")
        buf.write("\3\2\2\2\t\u008b\3\2\2\2\13\u0092\3\2\2\2\r\u0094\3\2")
        buf.write("\2\2\17\u009e\3\2\2\2\21\u00a7\3\2\2\2\23\u00af\3\2\2")
        buf.write("\2\25\u00ba\3\2\2\2\27\u00bf\3\2\2\2\31\u00c3\3\2\2\2")
        buf.write("\33\u00cb\3\2\2\2\35\u00d0\3\2\2\2\37\u00d9\3\2\2\2!\u00e3")
        buf.write("\3\2\2\2#\u00e8\3\2\2\2%\u00f1\3\2\2\2\'\u00f6\3\2\2\2")
        buf.write(")\u00fa\3\2\2\2+\u00fd\3\2\2\2-\u0102\3\2\2\2/\u0107\3")
        buf.write("\2\2\2\61\u010e\3\2\2\2\63\u0114\3\2\2\2\65\u0116\3\2")
        buf.write("\2\2\67\u0119\3\2\2\29\u011e\3\2\2\2;\u0124\3\2\2\2=\u012b")
        buf.write("\3\2\2\2?\u012d\3\2\2\2A\u0130\3\2\2\2C\u013b\3\2\2\2")
        buf.write("E\u0146\3\2\2\2G\u0148\3\2\2\2I\u0150\3\2\2\2K\u0152\3")
        buf.write("\2\2\2M\u0154\3\2\2\2O\u0156\3\2\2\2Q\u0158\3\2\2\2S\u015b")
        buf.write("\3\2\2\2U\u015e\3\2\2\2W\u0160\3\2\2\2Y\u0163\3\2\2\2")
        buf.write("[\u0165\3\2\2\2]\u0167\3\2\2\2_\u0169\3\2\2\2a\u016b\3")
        buf.write("\2\2\2c\u016e\3\2\2\2e\u0171\3\2\2\2g\u0173\3\2\2\2i\u0176")
        buf.write("\3\2\2\2k\u0178\3\2\2\2m\u017a\3\2\2\2o\u017c\3\2\2\2")
        buf.write("q\u017e\3\2\2\2s\u0180\3\2\2\2u\u0182\3\2\2\2w\u0184\3")
        buf.write("\2\2\2y\u0187\3\2\2\2{\u018d\3\2\2\2}\u019b\3\2\2\2\177")
        buf.write("\u01a6\3\2\2\2\u0081\u01a8\3\2\2\2\u0083\u01aa\3\2\2\2")
        buf.write("\u0085\u0086\3\2\2\2\u0086\4\3\2\2\2\u0087\u0088\3\2\2")
        buf.write("\2\u0088\6\3\2\2\2\u0089\u008a\3\2\2\2\u008a\b\3\2\2\2")
        buf.write("\u008b\u008c\3\2\2\2\u008c\n\3\2\2\2\u008d\u0093\5\r\7")
        buf.write("\2\u008e\u0093\5\17\b\2\u008f\u0093\5\21\t\2\u0090\u0093")
        buf.write("\5\25\13\2\u0091\u0093\5\t\5\2\u0092\u008d\3\2\2\2\u0092")
        buf.write("\u008e\3\2\2\2\u0092\u008f\3\2\2\2\u0092\u0090\3\2\2\2")
        buf.write("\u0092\u0091\3\2\2\2\u0093\f\3\2\2\2\u0094\u0095\5)\25")
        buf.write("\2\u0095\u0096\5m\67\2\u0096\u0097\5\7\4\2\u0097\u0098")
        buf.write("\5o8\2\u0098\u009c\5\13\6\2\u0099\u009a\5-\27\2\u009a")
        buf.write("\u009b\5\13\6\2\u009b\u009d\3\2\2\2\u009c\u0099\3\2\2")
        buf.write("\2\u009c\u009d\3\2\2\2\u009d\16\3\2\2\2\u009e\u009f\5")
        buf.write("\'\24\2\u009f\u00a0\5m\67\2\u00a0\u00a1\5\5\3\2\u00a1")
        buf.write("\u00a2\5u;\2\u00a2\u00a3\5\7\4\2\u00a3\u00a4\5u;\2\u00a4")
        buf.write("\u00a5\5\5\3\2\u00a5\u00a6\5o8\2\u00a6\20\3\2\2\2\u00a7")
        buf.write("\u00a8\7d\2\2\u00a8\u00a9\7t\2\2\u00a9\u00aa\7g\2\2\u00aa")
        buf.write("\u00ab\7c\2\2\u00ab\u00ac\7m\2\2\u00ac\u00ad\3\2\2\2\u00ad")
        buf.write("\u00ae\5u;\2\u00ae\22\3\2\2\2\u00af\u00b0\7e\2\2\u00b0")
        buf.write("\u00b1\7q\2\2\u00b1\u00b2\7p\2\2\u00b2\u00b3\7v\2\2\u00b3")
        buf.write("\u00b4\7k\2\2\u00b4\u00b5\7p\2\2\u00b5\u00b6\7w\2\2\u00b6")
        buf.write("\u00b7\7g\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00b9\5u;\2\u00b9")
        buf.write("\24\3\2\2\2\u00ba\u00bb\5\65\33\2\u00bb\u00bc\5\13\6\2")
        buf.write("\u00bc\u00bd\5\61\31\2\u00bd\u00be\5\3\2\2\u00be\26\3")
        buf.write("\2\2\2\u00bf\u00c0\7k\2\2\u00c0\u00c1\7p\2\2\u00c1\u00c2")
        buf.write("\7v\2\2\u00c2\30\3\2\2\2\u00c3\u00c4\7d\2\2\u00c4\u00c5")
        buf.write("\7q\2\2\u00c5\u00c6\7q\2\2\u00c6\u00c7\7n\2\2\u00c7\u00c8")
        buf.write("\7g\2\2\u00c8\u00c9\7c\2\2\u00c9\u00ca\7p\2\2\u00ca\32")
        buf.write("\3\2\2\2\u00cb\u00cc\7x\2\2\u00cc\u00cd\7q\2\2\u00cd\u00ce")
        buf.write("\7k\2\2\u00ce\u00cf\7f\2\2\u00cf\34\3\2\2\2\u00d0\u00d1")
        buf.write("\7h\2\2\u00d1\u00d2\7n\2\2\u00d2\u00d3\7q\2\2\u00d3\u00d4")
        buf.write("\7c\2\2\u00d4\u00d5\7v\2\2\u00d5\36\3\2\2\2\u00d6\u00da")
        buf.write("\5\27\f\2\u00d7\u00da\5\31\r\2\u00d8\u00da\5\35\17\2\u00d9")
        buf.write("\u00d6\3\2\2\2\u00d9\u00d7\3\2\2\2\u00d9\u00d8\3\2\2\2")
        buf.write("\u00da\u00db\3\2\2\2\u00db\u00dc\5;\36\2\u00dc\u00dd\5")
        buf.write("i\65\2\u00dd\u00de\5A!\2\u00de\u00df\5k\66\2\u00df\u00e0")
        buf.write("\5u;\2\u00e0 \3\2\2\2\u00e1\u00e4\5#\22\2\u00e2\u00e4")
        buf.write("\5%\23\2\u00e3\u00e1\3\2\2\2\u00e3\u00e2\3\2\2\2\u00e4")
        buf.write("\"\3\2\2\2\u00e5\u00e9\5\27\f\2\u00e6\u00e9\5\31\r\2\u00e7")
        buf.write("\u00e9\5\35\17\2\u00e8\u00e5\3\2\2\2\u00e8\u00e6\3\2\2")
        buf.write("\2\u00e8\u00e7\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\u00eb")
        buf.write("\5;\36\2\u00eb\u00ec\5i\65\2\u00ec\u00ed\5k\66\2\u00ed")
        buf.write("$\3\2\2\2\u00ee\u00f2\5\27\f\2\u00ef\u00f2\5\31\r\2\u00f0")
        buf.write("\u00f2\5\35\17\2\u00f1\u00ee\3\2\2\2\u00f1\u00ef\3\2\2")
        buf.write("\2\u00f1\u00f0\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00f4")
        buf.write("\5i\65\2\u00f4\u00f5\5k\66\2\u00f5&\3\2\2\2\u00f6\u00f7")
        buf.write("\7h\2\2\u00f7\u00f8\7q\2\2\u00f8\u00f9\7t\2\2\u00f9(\3")
        buf.write("\2\2\2\u00fa\u00fb\7k\2\2\u00fb\u00fc\7h\2\2\u00fc*\3")
        buf.write("\2\2\2\u00fd\u00fe\7v\2\2\u00fe\u00ff\7j\2\2\u00ff\u0100")
        buf.write("\7g\2\2\u0100\u0101\7p\2\2\u0101,\3\2\2\2\u0102\u0103")
        buf.write("\7g\2\2\u0103\u0104\7n\2\2\u0104\u0105\7u\2\2\u0105\u0106")
        buf.write("\7g\2\2\u0106.\3\2\2\2\u0107\u0108\7t\2\2\u0108\u0109")
        buf.write("\7g\2\2\u0109\u010a\7v\2\2\u010a\u010b\7w\2\2\u010b\u010c")
        buf.write("\7t\2\2\u010c\u010d\7p\2\2\u010d\60\3\2\2\2\u010e\u010f")
        buf.write("\7y\2\2\u010f\u0110\7j\2\2\u0110\u0111\7k\2\2\u0111\u0112")
        buf.write("\7n\2\2\u0112\u0113\7g\2\2\u0113\62\3\2\2\2\u0114\u0115")
        buf.write("\5\33\16\2\u0115\64\3\2\2\2\u0116\u0117\7f\2\2\u0117\u0118")
        buf.write("\7q\2\2\u0118\66\3\2\2\2\u0119\u011a\7v\2\2\u011a\u011b")
        buf.write("\7t\2\2\u011b\u011c\7w\2\2\u011c\u011d\7g\2\2\u011d8\3")
        buf.write("\2\2\2\u011e\u011f\7h\2\2\u011f\u0120\7c\2\2\u0120\u0121")
        buf.write("\7n\2\2\u0121\u0122\7u\2\2\u0122\u0123\7g\2\2\u0123:\3")
        buf.write("\2\2\2\u0124\u0128\5=\37\2\u0125\u0127\5? \2\u0126\u0125")
        buf.write("\3\2\2\2\u0127\u012a\3\2\2\2\u0128\u0126\3\2\2\2\u0128")
        buf.write("\u0129\3\2\2\2\u0129<\3\2\2\2\u012a\u0128\3\2\2\2\u012b")
        buf.write("\u012c\t\2\2\2\u012c>\3\2\2\2\u012d\u012e\t\3\2\2\u012e")
        buf.write("@\3\2\2\2\u012f\u0131\t\4\2\2\u0130\u012f\3\2\2\2\u0131")
        buf.write("\u0132\3\2\2\2\u0132\u0130\3\2\2\2\u0132\u0133\3\2\2\2")
        buf.write("\u0133B\3\2\2\2\u0134\u0136\5E#\2\u0135\u0137\5G$\2\u0136")
        buf.write("\u0135\3\2\2\2\u0136\u0137\3\2\2\2\u0137\u013c\3\2\2\2")
        buf.write("\u0138\u0139\5A!\2\u0139\u013a\5G$\2\u013a\u013c\3\2\2")
        buf.write("\2\u013b\u0134\3\2\2\2\u013b\u0138\3\2\2\2\u013cD\3\2")
        buf.write("\2\2\u013d\u013e\5A!\2\u013e\u013f\7\60\2\2\u013f\u0147")
        buf.write("\3\2\2\2\u0140\u0141\7\60\2\2\u0141\u0147\5A!\2\u0142")
        buf.write("\u0143\5A!\2\u0143\u0144\7\60\2\2\u0144\u0145\5A!\2\u0145")
        buf.write("\u0147\3\2\2\2\u0146\u013d\3\2\2\2\u0146\u0140\3\2\2\2")
        buf.write("\u0146\u0142\3\2\2\2\u0147F\3\2\2\2\u0148\u014a\t\5\2")
        buf.write("\2\u0149\u014b\5[.\2\u014a\u0149\3\2\2\2\u014a\u014b\3")
        buf.write("\2\2\2\u014b\u014c\3\2\2\2\u014c\u014d\5A!\2\u014dH\3")
        buf.write("\2\2\2\u014e\u0151\5\67\34\2\u014f\u0151\59\35\2\u0150")
        buf.write("\u014e\3\2\2\2\u0150\u014f\3\2\2\2\u0151J\3\2\2\2\u0152")
        buf.write("\u0153\7-\2\2\u0153L\3\2\2\2\u0154\u0155\7,\2\2\u0155")
        buf.write("N\3\2\2\2\u0156\u0157\7#\2\2\u0157P\3\2\2\2\u0158\u0159")
        buf.write("\7~\2\2\u0159\u015a\7~\2\2\u015aR\3\2\2\2\u015b\u015c")
        buf.write("\7#\2\2\u015c\u015d\7?\2\2\u015dT\3\2\2\2\u015e\u015f")
        buf.write("\7>\2\2\u015fV\3\2\2\2\u0160\u0161\7>\2\2\u0161\u0162")
        buf.write("\7?\2\2\u0162X\3\2\2\2\u0163\u0164\7?\2\2\u0164Z\3\2\2")
        buf.write("\2\u0165\u0166\7/\2\2\u0166\\\3\2\2\2\u0167\u0168\7\61")
        buf.write("\2\2\u0168^\3\2\2\2\u0169\u016a\7\'\2\2\u016a`\3\2\2\2")
        buf.write("\u016b\u016c\7(\2\2\u016c\u016d\7(\2\2\u016db\3\2\2\2")
        buf.write("\u016e\u016f\7?\2\2\u016f\u0170\7?\2\2\u0170d\3\2\2\2")
        buf.write("\u0171\u0172\7@\2\2\u0172f\3\2\2\2\u0173\u0174\7@\2\2")
        buf.write("\u0174\u0175\7?\2\2\u0175h\3\2\2\2\u0176\u0177\7]\2\2")
        buf.write("\u0177j\3\2\2\2\u0178\u0179\7_\2\2\u0179l\3\2\2\2\u017a")
        buf.write("\u017b\7*\2\2\u017bn\3\2\2\2\u017c\u017d\7+\2\2\u017d")
        buf.write("p\3\2\2\2\u017e\u017f\7}\2\2\u017fr\3\2\2\2\u0180\u0181")
        buf.write("\7\177\2\2\u0181t\3\2\2\2\u0182\u0183\7=\2\2\u0183v\3")
        buf.write("\2\2\2\u0184\u0185\7.\2\2\u0185x\3\2\2\2\u0186\u0188\t")
        buf.write("\6\2\2\u0187\u0186\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u0187")
        buf.write("\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u018b\3\2\2\2\u018b")
        buf.write("\u018c\b=\2\2\u018cz\3\2\2\2\u018d\u018e\7\61\2\2\u018e")
        buf.write("\u018f\7,\2\2\u018f\u0193\3\2\2\2\u0190\u0192\13\2\2\2")
        buf.write("\u0191\u0190\3\2\2\2\u0192\u0195\3\2\2\2\u0193\u0194\3")
        buf.write("\2\2\2\u0193\u0191\3\2\2\2\u0194\u0196\3\2\2\2\u0195\u0193")
        buf.write("\3\2\2\2\u0196\u0197\7,\2\2\u0197\u0198\7\61\2\2\u0198")
        buf.write("\u0199\3\2\2\2\u0199\u019a\b>\2\2\u019a|\3\2\2\2\u019b")
        buf.write("\u019c\7\61\2\2\u019c\u019d\7\61\2\2\u019d\u01a1\3\2\2")
        buf.write("\2\u019e\u01a0\13\2\2\2\u019f\u019e\3\2\2\2\u01a0\u01a3")
        buf.write("\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a1\u019f\3\2\2\2\u01a2")
        buf.write("\u01a4\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a4\u01a5\b?\2\2")
        buf.write("\u01a5~\3\2\2\2\u01a6\u01a7\13\2\2\2\u01a7\u0080\3\2\2")
        buf.write("\2\u01a8\u01a9\13\2\2\2\u01a9\u0082\3\2\2\2\u01aa\u01ab")
        buf.write("\13\2\2\2\u01ab\u0084\3\2\2\2\23\2\u0092\u009c\u00d9\u00e3")
        buf.write("\u00e8\u00f1\u0128\u0132\u0136\u013b\u0146\u014a\u0150")
        buf.write("\u0189\u0193\u01a1\3\b\2\2")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    EXP = 1
    EXPINT = 2
    EXPBL = 3
    EXPSMT = 4
    SMT = 5
    IFSMT = 6
    FORSMT = 7
    BREAKSt = 8
    CONTINUESt = 9
    DOWHILESMT = 10
    INTTYPE = 11
    BOOLEAN = 12
    VOIDTYPE = 13
    FLOATTYPE = 14
    ARRAYTYPE = 15
    ARRAYPTTYPE = 16
    Inparr = 17
    Outarr = 18
    FOR = 19
    IF = 20
    THEN = 21
    ELSE = 22
    RETURN = 23
    WHILE = 24
    VOID = 25
    DO = 26
    TRUE = 27
    FALSE = 28
    ID = 29
    INTLIT = 30
    FLOATLIT = 31
    BOOLIT = 32
    ADD = 33
    MUL = 34
    LOGN = 35
    LOGO = 36
    NOTE = 37
    LT = 38
    LTOE = 39
    ASSIG = 40
    SUB = 41
    DIV = 42
    MOD = 43
    LOGA = 44
    EQ = 45
    GT = 46
    GTOE = 47
    LSB = 48
    RSB = 49
    LB = 50
    RB = 51
    LP = 52
    RP = 53
    SEMI = 54
    CM = 55
    WS = 56
    BLOCKCMT = 57
    LINECMT = 58
    ERROR_CHAR = 59
    UNCLOSE_STRING = 60
    ILLEGAL_ESCAPE = 61

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'boolean'", "'void'", "'float'", "'for'", "'if'", 
            "'then'", "'else'", "'return'", "'while'", "'do'", "'true'", 
            "'false'", "'+'", "'*'", "'!'", "'||'", "'!='", "'<'", "'<='", 
            "'='", "'-'", "'/'", "'%'", "'&&'", "'=='", "'>'", "'>='", "'['", 
            "']'", "'('", "')'", "'{'", "'}'", "';'", "','" ]

    symbolicNames = [ "<INVALID>",
            "EXP", "EXPINT", "EXPBL", "EXPSMT", "SMT", "IFSMT", "FORSMT", 
            "BREAKSt", "CONTINUESt", "DOWHILESMT", "INTTYPE", "BOOLEAN", 
            "VOIDTYPE", "FLOATTYPE", "ARRAYTYPE", "ARRAYPTTYPE", "Inparr", 
            "Outarr", "FOR", "IF", "THEN", "ELSE", "RETURN", "WHILE", "VOID", 
            "DO", "TRUE", "FALSE", "ID", "INTLIT", "FLOATLIT", "BOOLIT", 
            "ADD", "MUL", "LOGN", "LOGO", "NOTE", "LT", "LTOE", "ASSIG", 
            "SUB", "DIV", "MOD", "LOGA", "EQ", "GT", "GTOE", "LSB", "RSB", 
            "LB", "RB", "LP", "RP", "SEMI", "CM", "WS", "BLOCKCMT", "LINECMT", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "EXP", "EXPINT", "EXPBL", "EXPSMT", "SMT", "IFSMT", "FORSMT", 
                  "BREAKSt", "CONTINUESt", "DOWHILESMT", "INTTYPE", "BOOLEAN", 
                  "VOIDTYPE", "FLOATTYPE", "ARRAYTYPE", "ARRAYPTTYPE", "Inparr", 
                  "Outarr", "FOR", "IF", "THEN", "ELSE", "RETURN", "WHILE", 
                  "VOID", "DO", "TRUE", "FALSE", "ID", "Letter", "LetterOrDigit", 
                  "INTLIT", "FLOATLIT", "NUMPART", "DECPART", "BOOLIT", 
                  "ADD", "MUL", "LOGN", "LOGO", "NOTE", "LT", "LTOE", "ASSIG", 
                  "SUB", "DIV", "MOD", "LOGA", "EQ", "GT", "GTOE", "LSB", 
                  "RSB", "LB", "RB", "LP", "RP", "SEMI", "CM", "WS", "BLOCKCMT", 
                  "LINECMT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


