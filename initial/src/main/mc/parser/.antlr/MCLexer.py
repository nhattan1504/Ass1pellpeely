# Generated from /home/ktant/Documents/PPL/assignment1/initial/src/main/mc/parser/MC.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\64")
        buf.write("\u0174\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\3\2\3\2\5\2x\n\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\7\23\u00d2\n\23\f\23\16")
        buf.write("\23\u00d5\13\23\3\24\3\24\3\25\3\25\3\26\6\26\u00dc\n")
        buf.write("\26\r\26\16\26\u00dd\3\27\3\27\5\27\u00e2\n\27\3\27\3")
        buf.write("\27\3\27\5\27\u00e7\n\27\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\5\30\u00f2\n\30\3\31\3\31\5\31\u00f6\n")
        buf.write("\31\3\31\3\31\3\32\3\32\5\32\u00fc\n\32\3\32\3\32\3\32")
        buf.write("\3\33\6\33\u0102\n\33\r\33\16\33\u0103\3\34\3\34\5\34")
        buf.write("\u0108\n\34\3\35\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3")
        buf.write("!\3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3&\3&\3\'\3\'")
        buf.write("\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3,\3,\3,\3-\3-\3.\3.\3")
        buf.write("/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\65\6\65\u0142\n\65\r\65\16\65\u0143\3\65\3\65\3\66")
        buf.write("\3\66\3\66\3\66\7\66\u014c\n\66\f\66\16\66\u014f\13\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\7\67\u015a")
        buf.write("\n\67\f\67\16\67\u015d\13\67\3\67\3\67\38\38\58\u0163")
        buf.write("\n8\38\58\u0166\n8\38\38\39\39\59\u016c\n9\39\39\39\3")
        buf.write("9\39\3:\3:\3\u014d\2;\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\2)\2+\25-\26/\2\61\2\63\27\65\2\67\29\2;\30=\31?\32")
        buf.write("A\33C\34E\35G\36I\37K M!O\"Q#S$U%W&Y\'[(])_*a+c,e-g.i")
        buf.write("/k\60m\61o\62q\63s\64\3\2\f\5\2C\\aac|\6\2\62;C\\aac|")
        buf.write("\3\2\62;\4\2GGgg\6\2\f\f\17\17$$^^\n\2$$))^^ddhhppttv")
        buf.write("v\5\2\13\f\17\17\"\"\4\2\f\f\17\17\4\3\f\f\17\17\t\2$")
        buf.write("$^^ddhhppttvv\2\u017c\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2")
        buf.write("\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!")
        buf.write("\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write("\63\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_")
        buf.write("\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2")
        buf.write("i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2")
        buf.write("\2s\3\2\2\2\3w\3\2\2\2\5y\3\2\2\2\7}\3\2\2\2\t\u0085\3")
        buf.write("\2\2\2\13\u008a\3\2\2\2\r\u0090\3\2\2\2\17\u0094\3\2\2")
        buf.write("\2\21\u0097\3\2\2\2\23\u009c\3\2\2\2\25\u00a3\3\2\2\2")
        buf.write("\27\u00a9\3\2\2\2\31\u00ab\3\2\2\2\33\u00ae\3\2\2\2\35")
        buf.write("\u00b3\3\2\2\2\37\u00b9\3\2\2\2!\u00c0\3\2\2\2#\u00c6")
        buf.write("\3\2\2\2%\u00cf\3\2\2\2\'\u00d6\3\2\2\2)\u00d8\3\2\2\2")
        buf.write("+\u00db\3\2\2\2-\u00e6\3\2\2\2/\u00f1\3\2\2\2\61\u00f3")
        buf.write("\3\2\2\2\63\u00f9\3\2\2\2\65\u0101\3\2\2\2\67\u0107\3")
        buf.write("\2\2\29\u0109\3\2\2\2;\u010c\3\2\2\2=\u010e\3\2\2\2?\u0110")
        buf.write("\3\2\2\2A\u0112\3\2\2\2C\u0115\3\2\2\2E\u0118\3\2\2\2")
        buf.write("G\u011a\3\2\2\2I\u011d\3\2\2\2K\u011f\3\2\2\2M\u0121\3")
        buf.write("\2\2\2O\u0123\3\2\2\2Q\u0125\3\2\2\2S\u0128\3\2\2\2U\u012b")
        buf.write("\3\2\2\2W\u012d\3\2\2\2Y\u0130\3\2\2\2[\u0132\3\2\2\2")
        buf.write("]\u0134\3\2\2\2_\u0136\3\2\2\2a\u0138\3\2\2\2c\u013a\3")
        buf.write("\2\2\2e\u013c\3\2\2\2g\u013e\3\2\2\2i\u0141\3\2\2\2k\u0147")
        buf.write("\3\2\2\2m\u0155\3\2\2\2o\u0160\3\2\2\2q\u0169\3\2\2\2")
        buf.write("s\u0172\3\2\2\2ux\5\33\16\2vx\5\35\17\2wu\3\2\2\2wv\3")
        buf.write("\2\2\2x\4\3\2\2\2yz\7k\2\2z{\7p\2\2{|\7v\2\2|\6\3\2\2")
        buf.write("\2}~\7d\2\2~\177\7q\2\2\177\u0080\7q\2\2\u0080\u0081\7")
        buf.write("n\2\2\u0081\u0082\7g\2\2\u0082\u0083\7c\2\2\u0083\u0084")
        buf.write("\7p\2\2\u0084\b\3\2\2\2\u0085\u0086\7x\2\2\u0086\u0087")
        buf.write("\7q\2\2\u0087\u0088\7k\2\2\u0088\u0089\7f\2\2\u0089\n")
        buf.write("\3\2\2\2\u008a\u008b\7h\2\2\u008b\u008c\7n\2\2\u008c\u008d")
        buf.write("\7q\2\2\u008d\u008e\7c\2\2\u008e\u008f\7v\2\2\u008f\f")
        buf.write("\3\2\2\2\u0090\u0091\7h\2\2\u0091\u0092\7q\2\2\u0092\u0093")
        buf.write("\7t\2\2\u0093\16\3\2\2\2\u0094\u0095\7k\2\2\u0095\u0096")
        buf.write("\7h\2\2\u0096\20\3\2\2\2\u0097\u0098\7g\2\2\u0098\u0099")
        buf.write("\7n\2\2\u0099\u009a\7u\2\2\u009a\u009b\7g\2\2\u009b\22")
        buf.write("\3\2\2\2\u009c\u009d\7t\2\2\u009d\u009e\7g\2\2\u009e\u009f")
        buf.write("\7v\2\2\u009f\u00a0\7w\2\2\u00a0\u00a1\7t\2\2\u00a1\u00a2")
        buf.write("\7p\2\2\u00a2\24\3\2\2\2\u00a3\u00a4\7y\2\2\u00a4\u00a5")
        buf.write("\7j\2\2\u00a5\u00a6\7k\2\2\u00a6\u00a7\7n\2\2\u00a7\u00a8")
        buf.write("\7g\2\2\u00a8\26\3\2\2\2\u00a9\u00aa\5\t\5\2\u00aa\30")
        buf.write("\3\2\2\2\u00ab\u00ac\7f\2\2\u00ac\u00ad\7q\2\2\u00ad\32")
        buf.write("\3\2\2\2\u00ae\u00af\7v\2\2\u00af\u00b0\7t\2\2\u00b0\u00b1")
        buf.write("\7w\2\2\u00b1\u00b2\7g\2\2\u00b2\34\3\2\2\2\u00b3\u00b4")
        buf.write("\7h\2\2\u00b4\u00b5\7c\2\2\u00b5\u00b6\7n\2\2\u00b6\u00b7")
        buf.write("\7u\2\2\u00b7\u00b8\7g\2\2\u00b8\36\3\2\2\2\u00b9\u00ba")
        buf.write("\7u\2\2\u00ba\u00bb\7v\2\2\u00bb\u00bc\7t\2\2\u00bc\u00bd")
        buf.write("\7k\2\2\u00bd\u00be\7p\2\2\u00be\u00bf\7i\2\2\u00bf \3")
        buf.write("\2\2\2\u00c0\u00c1\7d\2\2\u00c1\u00c2\7t\2\2\u00c2\u00c3")
        buf.write("\7g\2\2\u00c3\u00c4\7c\2\2\u00c4\u00c5\7m\2\2\u00c5\"")
        buf.write("\3\2\2\2\u00c6\u00c7\7e\2\2\u00c7\u00c8\7q\2\2\u00c8\u00c9")
        buf.write("\7p\2\2\u00c9\u00ca\7v\2\2\u00ca\u00cb\7k\2\2\u00cb\u00cc")
        buf.write("\7p\2\2\u00cc\u00cd\7w\2\2\u00cd\u00ce\7g\2\2\u00ce$\3")
        buf.write("\2\2\2\u00cf\u00d3\5\'\24\2\u00d0\u00d2\5)\25\2\u00d1")
        buf.write("\u00d0\3\2\2\2\u00d2\u00d5\3\2\2\2\u00d3\u00d1\3\2\2\2")
        buf.write("\u00d3\u00d4\3\2\2\2\u00d4&\3\2\2\2\u00d5\u00d3\3\2\2")
        buf.write("\2\u00d6\u00d7\t\2\2\2\u00d7(\3\2\2\2\u00d8\u00d9\t\3")
        buf.write("\2\2\u00d9*\3\2\2\2\u00da\u00dc\t\4\2\2\u00db\u00da\3")
        buf.write("\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00db\3\2\2\2\u00dd\u00de")
        buf.write("\3\2\2\2\u00de,\3\2\2\2\u00df\u00e1\5/\30\2\u00e0\u00e2")
        buf.write("\5\61\31\2\u00e1\u00e0\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2")
        buf.write("\u00e7\3\2\2\2\u00e3\u00e4\5+\26\2\u00e4\u00e5\5\61\31")
        buf.write("\2\u00e5\u00e7\3\2\2\2\u00e6\u00df\3\2\2\2\u00e6\u00e3")
        buf.write("\3\2\2\2\u00e7.\3\2\2\2\u00e8\u00e9\5+\26\2\u00e9\u00ea")
        buf.write("\7\60\2\2\u00ea\u00f2\3\2\2\2\u00eb\u00ec\7\60\2\2\u00ec")
        buf.write("\u00f2\5+\26\2\u00ed\u00ee\5+\26\2\u00ee\u00ef\7\60\2")
        buf.write("\2\u00ef\u00f0\5+\26\2\u00f0\u00f2\3\2\2\2\u00f1\u00e8")
        buf.write("\3\2\2\2\u00f1\u00eb\3\2\2\2\u00f1\u00ed\3\2\2\2\u00f2")
        buf.write("\60\3\2\2\2\u00f3\u00f5\t\5\2\2\u00f4\u00f6\5K&\2\u00f5")
        buf.write("\u00f4\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f7\3\2\2\2")
        buf.write("\u00f7\u00f8\5+\26\2\u00f8\62\3\2\2\2\u00f9\u00fb\7$\2")
        buf.write("\2\u00fa\u00fc\5\65\33\2\u00fb\u00fa\3\2\2\2\u00fb\u00fc")
        buf.write("\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd\u00fe\7$\2\2\u00fe")
        buf.write("\u00ff\b\32\2\2\u00ff\64\3\2\2\2\u0100\u0102\5\67\34\2")
        buf.write("\u0101\u0100\3\2\2\2\u0102\u0103\3\2\2\2\u0103\u0101\3")
        buf.write("\2\2\2\u0103\u0104\3\2\2\2\u0104\66\3\2\2\2\u0105\u0108")
        buf.write("\n\6\2\2\u0106\u0108\59\35\2\u0107\u0105\3\2\2\2\u0107")
        buf.write("\u0106\3\2\2\2\u01088\3\2\2\2\u0109\u010a\7^\2\2\u010a")
        buf.write("\u010b\t\7\2\2\u010b:\3\2\2\2\u010c\u010d\7-\2\2\u010d")
        buf.write("<\3\2\2\2\u010e\u010f\7,\2\2\u010f>\3\2\2\2\u0110\u0111")
        buf.write("\7#\2\2\u0111@\3\2\2\2\u0112\u0113\7~\2\2\u0113\u0114")
        buf.write("\7~\2\2\u0114B\3\2\2\2\u0115\u0116\7#\2\2\u0116\u0117")
        buf.write("\7?\2\2\u0117D\3\2\2\2\u0118\u0119\7>\2\2\u0119F\3\2\2")
        buf.write("\2\u011a\u011b\7>\2\2\u011b\u011c\7?\2\2\u011cH\3\2\2")
        buf.write("\2\u011d\u011e\7?\2\2\u011eJ\3\2\2\2\u011f\u0120\7/\2")
        buf.write("\2\u0120L\3\2\2\2\u0121\u0122\7\61\2\2\u0122N\3\2\2\2")
        buf.write("\u0123\u0124\7\'\2\2\u0124P\3\2\2\2\u0125\u0126\7(\2\2")
        buf.write("\u0126\u0127\7(\2\2\u0127R\3\2\2\2\u0128\u0129\7?\2\2")
        buf.write("\u0129\u012a\7?\2\2\u012aT\3\2\2\2\u012b\u012c\7@\2\2")
        buf.write("\u012cV\3\2\2\2\u012d\u012e\7@\2\2\u012e\u012f\7?\2\2")
        buf.write("\u012fX\3\2\2\2\u0130\u0131\7]\2\2\u0131Z\3\2\2\2\u0132")
        buf.write("\u0133\7_\2\2\u0133\\\3\2\2\2\u0134\u0135\7*\2\2\u0135")
        buf.write("^\3\2\2\2\u0136\u0137\7+\2\2\u0137`\3\2\2\2\u0138\u0139")
        buf.write("\7}\2\2\u0139b\3\2\2\2\u013a\u013b\7\177\2\2\u013bd\3")
        buf.write("\2\2\2\u013c\u013d\7=\2\2\u013df\3\2\2\2\u013e\u013f\7")
        buf.write(".\2\2\u013fh\3\2\2\2\u0140\u0142\t\b\2\2\u0141\u0140\3")
        buf.write("\2\2\2\u0142\u0143\3\2\2\2\u0143\u0141\3\2\2\2\u0143\u0144")
        buf.write("\3\2\2\2\u0144\u0145\3\2\2\2\u0145\u0146\b\65\3\2\u0146")
        buf.write("j\3\2\2\2\u0147\u0148\7\61\2\2\u0148\u0149\7,\2\2\u0149")
        buf.write("\u014d\3\2\2\2\u014a\u014c\13\2\2\2\u014b\u014a\3\2\2")
        buf.write("\2\u014c\u014f\3\2\2\2\u014d\u014e\3\2\2\2\u014d\u014b")
        buf.write("\3\2\2\2\u014e\u0150\3\2\2\2\u014f\u014d\3\2\2\2\u0150")
        buf.write("\u0151\7,\2\2\u0151\u0152\7\61\2\2\u0152\u0153\3\2\2\2")
        buf.write("\u0153\u0154\b\66\3\2\u0154l\3\2\2\2\u0155\u0156\7\61")
        buf.write("\2\2\u0156\u0157\7\61\2\2\u0157\u015b\3\2\2\2\u0158\u015a")
        buf.write("\n\t\2\2\u0159\u0158\3\2\2\2\u015a\u015d\3\2\2\2\u015b")
        buf.write("\u0159\3\2\2\2\u015b\u015c\3\2\2\2\u015c\u015e\3\2\2\2")
        buf.write("\u015d\u015b\3\2\2\2\u015e\u015f\b\67\3\2\u015fn\3\2\2")
        buf.write("\2\u0160\u0162\7$\2\2\u0161\u0163\5\65\33\2\u0162\u0161")
        buf.write("\3\2\2\2\u0162\u0163\3\2\2\2\u0163\u0165\3\2\2\2\u0164")
        buf.write("\u0166\t\n\2\2\u0165\u0164\3\2\2\2\u0166\u0167\3\2\2\2")
        buf.write("\u0167\u0168\b8\4\2\u0168p\3\2\2\2\u0169\u016b\7$\2\2")
        buf.write("\u016a\u016c\5\65\33\2\u016b\u016a\3\2\2\2\u016b\u016c")
        buf.write("\3\2\2\2\u016c\u016d\3\2\2\2\u016d\u016e\7^\2\2\u016e")
        buf.write("\u016f\n\13\2\2\u016f\u0170\3\2\2\2\u0170\u0171\b9\5\2")
        buf.write("\u0171r\3\2\2\2\u0172\u0173\13\2\2\2\u0173t\3\2\2\2\23")
        buf.write("\2w\u00d3\u00dd\u00e1\u00e6\u00f1\u00f5\u00fb\u0103\u0107")
        buf.write("\u0143\u014d\u015b\u0162\u0165\u016b\6\3\32\2\b\2\2\3")
        buf.write("8\3\39\4")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BOOLIT = 1
    INTTYPE = 2
    BOOLEAN = 3
    VOIDTYPE = 4
    FLOATTYPE = 5
    FOR = 6
    IF = 7
    ELSE = 8
    RETURN = 9
    WHILE = 10
    VOID = 11
    DO = 12
    TRUE = 13
    FALSE = 14
    STRINGTYPE = 15
    BREAK = 16
    CONTINUE = 17
    ID = 18
    INTLIT = 19
    FLOATLIT = 20
    STRINGLIT = 21
    ADD = 22
    MUL = 23
    LOGN = 24
    LOGO = 25
    NOTE = 26
    LT = 27
    LTOE = 28
    ASSIG = 29
    SUB = 30
    DIV = 31
    MOD = 32
    LOGA = 33
    EQ = 34
    GT = 35
    GTOE = 36
    LSB = 37
    RSB = 38
    LB = 39
    RB = 40
    LP = 41
    RP = 42
    SEMI = 43
    CM = 44
    WS = 45
    BLOCKCMT = 46
    LINECMT = 47
    UNCLOSE_STRING = 48
    ILLEGAL_ESCAPE = 49
    ERROR_CHAR = 50

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'boolean'", "'void'", "'float'", "'for'", "'if'", 
            "'else'", "'return'", "'while'", "'do'", "'true'", "'false'", 
            "'string'", "'break'", "'continue'", "'+'", "'*'", "'!'", "'||'", 
            "'!='", "'<'", "'<='", "'='", "'-'", "'/'", "'%'", "'&&'", "'=='", 
            "'>'", "'>='", "'['", "']'", "'('", "')'", "'{'", "'}'", "';'", 
            "','" ]

    symbolicNames = [ "<INVALID>",
            "BOOLIT", "INTTYPE", "BOOLEAN", "VOIDTYPE", "FLOATTYPE", "FOR", 
            "IF", "ELSE", "RETURN", "WHILE", "VOID", "DO", "TRUE", "FALSE", 
            "STRINGTYPE", "BREAK", "CONTINUE", "ID", "INTLIT", "FLOATLIT", 
            "STRINGLIT", "ADD", "MUL", "LOGN", "LOGO", "NOTE", "LT", "LTOE", 
            "ASSIG", "SUB", "DIV", "MOD", "LOGA", "EQ", "GT", "GTOE", "LSB", 
            "RSB", "LB", "RB", "LP", "RP", "SEMI", "CM", "WS", "BLOCKCMT", 
            "LINECMT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "BOOLIT", "INTTYPE", "BOOLEAN", "VOIDTYPE", "FLOATTYPE", 
                  "FOR", "IF", "ELSE", "RETURN", "WHILE", "VOID", "DO", 
                  "TRUE", "FALSE", "STRINGTYPE", "BREAK", "CONTINUE", "ID", 
                  "Letter", "LetterOrDigit", "INTLIT", "FLOATLIT", "NUMPART", 
                  "DECPART", "STRINGLIT", "Strings", "String", "Escape", 
                  "ADD", "MUL", "LOGN", "LOGO", "NOTE", "LT", "LTOE", "ASSIG", 
                  "SUB", "DIV", "MOD", "LOGA", "EQ", "GT", "GTOE", "LSB", 
                  "RSB", "LB", "RB", "LP", "RP", "SEMI", "CM", "WS", "BLOCKCMT", 
                  "LINECMT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[24] = self.STRINGLIT_action 
            actions[54] = self.UNCLOSE_STRING_action 
            actions[55] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text=self.text.strip('"')
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text=self.text.lstrip('"').rstrip("\n\r")
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text=self.text.lstrip('"')
     


