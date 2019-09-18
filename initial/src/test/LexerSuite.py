import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_identifier_1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(" _abc___ ","_abc___,<EOF>",101))    
    def test_identifier_2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(" abcda ","abcda,<EOF>",102))
    def test_identifier_3(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(" abc234abc__234abc ","abc234abc__234abc,<EOF>",103))
    def test_identifier_4(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(" abc_123 123_abc/* abc */ ","abc_123,123,_abc,<EOF>",104))

    def test_identifier_5(self):
        self.assertTrue(TestLexer.checkLexeme(" aCBbdccdc ","aCBbdccdc,<EOF>",105))
    def test_identifier_6(self):
        self.assertTrue(TestLexer.checkLexeme("qwertyQWERTY ","qwertyQWERTY,<EOF>",106))

    def test_eror_token_1(self):
        self.assertTrue(TestLexer.checkLexeme(" aA?sVN ","aA,Error Token ?",107))
    def test_eror_token_2(self):
        self.assertTrue(TestLexer.checkLexeme(" nh@t t@ nguyen#a ","nh,Error Token @",108))
    def test_eror_token_3(self):
        self.assertTrue(TestLexer.checkLexeme(" t$nkdsa ","t,Error Token $",109))
    def test_eror_token_4(self):
        self.assertTrue(TestLexer.checkLexeme(" nguyen nh@t tan ","nguyen,nh,Error Token @",110))

    def test_keywork_1(self):
        """test keywork"""
        self.assertTrue(TestLexer.checkLexeme(" boolean if  int float return string ","boolean,if,int,float,return,string,<EOF>",111))
    def test_keywork_2(self):
        """test keywork"""
        self.assertTrue(TestLexer.checkLexeme(" BOOLEAN IF MAin iNt fLoat  ","BOOLEAN,IF,MAin,iNt,fLoat,<EOF>",112))
    def test_keywork_3(self):
        """test keywork"""
        self.assertTrue(TestLexer.checkLexeme(" IF ELSE iF eLse if else If ELse ","IF,ELSE,iF,eLse,if,else,If,ELse,<EOF>",113))
    def test_keywork_4(self):
        """test keywork"""
        self.assertTrue(TestLexer.checkLexeme(" while whILe WhiLE wHILe ","while,whILe,WhiLE,wHILe,<EOF>",114))
    def test_keywork_5(self):
        """test keywork"""
        self.assertTrue(TestLexer.checkLexeme(" intEgeR Float StrIng BoOleaN ","intEgeR,Float,StrIng,BoOleaN,<EOF>",115))
    def test_keywork_6(self):
        """test keywork"""
        self.assertTrue(TestLexer.checkLexeme("  else for float if boolean break continue int return void do while true false string ","else,for,float,if,boolean,break,continue,int,return,void,do,while,true,false,string,<EOF>",116))

    def test_integer_1(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme(" 123a123 ","123,a123,<EOF>",117))
    def test_integer_2(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme(" 13 0 100 69 893218 999999 abc123 ","13,0,100,69,893218,999999,abc123,<EOF>",118))
    def test_integer_3(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("1321_djmiska","1321,_djmiska,<EOF>",119))
    def test_integer_4(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("1343315__mdska123","1343315,__mdska123,<EOF>",120))
    def test_integer_5(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("-134641881","-,134641881,<EOF>",121))
    def test_integer_6(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("~123","Error Token ~",122))
    def test_integer_7(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme(" 1634667-4667 ","1634667,-,4667,<EOF>",123))
    def test_integer_8(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme(" 123/1112~456 ","123,/,1112,Error Token ~",124))
    def test_integer_9(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme(" 12-123 ","12,-,123,<EOF>",125))
    def test_integer_10(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme(" a123*123 ","a123,*,123,<EOF>",126))


    def test_operators_1(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme(" a == a + b ","a,==,a,+,b,<EOF>",127))
    def test_operators_2(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme("a*b+c-d","a,*,b,+,c,-,d,<EOF>",128))
    def test_operators_3(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme("a=1+3*4","a,=,1,+,3,*,4,<EOF>",129))
    def test_operators_4(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme(" abc/*123 ","abc,/,*,123,<EOF>",130))
    def test_operators_5(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme(" 123%dsad ","123,%,dsad,<EOF>",131))
    def test_operators_6(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme(" a&&b<c ","a,&&,b,<,c,<EOF>",132))
    def test_operators_7(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme(" a!=y<g ","a,!=,y,<,g,<EOF>",133))
    def test_operators_8(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme(" duk-||%","duk,-,||,%,<EOF>",134))
    def test_operators_9(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme(" 1dsad!=km!1 ","1,dsad,!=,km,!,1,<EOF>",135))
    def test_operators_10(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme(" x=a+b-c%!de","x,=,a,+,b,-,c,%,!,de,<EOF>",136))


    def test_floatl_1(self):
        """test floatl"""
        self.assertTrue(TestLexer.checkLexeme("12.e1 1.e-5 1.0e-12 ","12.e1,1.e-5,1.0e-12,<EOF>",138))
    def test_floatl_2(self):
        """test floatl"""
        self.assertTrue(TestLexer.checkLexeme(" 12e 12.e .3e-4 ","12,e,12.,e,.3e-4,<EOF>",139))
    def test_floatl_3(self):
        """test floatl"""
        self.assertTrue(TestLexer.checkLexeme(" 1.e -01.e-1 -1e-3.0 ","1.,e,-,01.e-1,-,1e-3,.0,<EOF>",140))
    def test_floatl_4(self):
        """test floatl"""
        self.assertTrue(TestLexer.checkLexeme(" .1 1. 12e 0.e-10 ",".1,1.,12,e,0.e-10,<EOF>",141))
    def test_floatl_5(self):
        """test floatl"""
        self.assertTrue(TestLexer.checkLexeme(" .e5 ","Error Token .",142))
    def test_floatl_6(self):
        """test floatl"""
        self.assertTrue(TestLexer.checkLexeme(" 1.25678 ","1.25678,<EOF>",143))
    def test_floatl_7(self):
        """test floatl"""
        self.assertTrue(TestLexer.checkLexeme(" 12.e12-3 ","12.e12,-,3,<EOF>",144))
    def test_floatl_8(self):
        """test floatl"""
        self.assertTrue(TestLexer.checkLexeme(" 12.e12abcs ","12.e12,abcs,<EOF>",145))
    def test_floatl_9(self):
        # """test floatl"""
        self.assertTrue(TestLexer.checkLexeme(" -123.e- ","-,123.,e,-,<EOF>",146))
    def test_floatl_10(self):
        """test floatl"""
        self.assertTrue(TestLexer.checkLexeme(" -897.e-123  ","-,897.e-123,<EOF>",147))
    def test_floatl_11(self):
        """test floatl"""
        self.assertTrue(TestLexer.checkLexeme(" -12.e+98 ","-,12.,e,+,98,<EOF>",148))

    def test_block_comment_1(self):
        """test block comment"""
        self.assertTrue(TestLexer.checkLexeme("/* pass PPL */","<EOF>",149))
    def test_block_comment_2(self):
        """test block comment"""
        self.assertTrue(TestLexer.checkLexeme("/* //aaaaaaaa */","<EOF>",150))
    def test_block_comment_3(self):
        """test block comment"""
        self.assertTrue(TestLexer.checkLexeme("/* /*aaaaaaaaabcdef */","<EOF>",151))
    def test_block_comment_4(self):
        """test block comment"""
        self.assertTrue(TestLexer.checkLexeme(" /* tandz ","/,*,tandz,<EOF>",152))
    def test_block_comment_5(self):
        """test block comment"""
        self.assertTrue(TestLexer.checkLexeme(" // /*ppl// */ ","<EOF>",153))

    def test_line_comment_1(self):
        """test line comment"""
        self.assertTrue(TestLexer.checkLexeme("//abcdef ","<EOF>",154))
    def test_line_comment_2(self):
        """test line comment"""
        self.assertTrue(TestLexer.checkLexeme("//abcdef  /* asadasdas */","<EOF>",155))
    def test_line_comment_3(self):
        """test line comment"""
        self.assertTrue(TestLexer.checkLexeme("//abcdef //////*****/ 123456","<EOF>",156))
    def test_line_comment_4(self):
        """test line comment"""
        self.assertTrue(TestLexer.checkLexeme("123abc.eas//abcdef /* asadasdas */","123,abc,Error Token .",157))
    def test_line_comment_5(self):
        """test line comment"""
        self.assertTrue(TestLexer.checkLexeme(" //abc \\n bef ","<EOF>",158))
    

    def test_separators_1(self):
        """test separators"""
        self.assertTrue(TestLexer.checkLexeme(""" [ba[b]a[ba][a]b[ab][a] ""","[,ba,[,b,],a,[,ba,],[,a,],b,[,ab,],[,a,],<EOF>",159))
    def test_separators_2(self):
        """test separators"""
        self.assertTrue(TestLexer.checkLexeme(" .adsabh. ","Error Token .",160))
    def test_separators_3(self):
        """test separators"""
        self.assertTrue(TestLexer.checkLexeme(" ","abc,;,def,,,nguyen,;,;,,,<EOF>",161))
    
    def test_separators_4(self):
        """test separators"""
        self.assertTrue(TestLexer.checkLexeme("//';';'{{(([]))}} ","<EOF>",162))
    # def test_separators_5(self):
    #     """test separators"""
    #     self.assertTrue(TestLexer.checkLexeme(""" { ] ( ; . , ""","{,],(,;,Error Token .",152))

 
    # def test_string_1(self):
    #     """test string"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "123a\\n123" ""","""123a\\n123,<EOF>""",163))
    # def test_string_2(self):
    #     """test string"""
    #     self.assertTrue(TestLexer.checkLexeme(""" abcdef"abc"123_15 ""","""abcdef,abc,123,_15,<EOF>""",164))
    # def test_string_3(self):
    #     """test string"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "abc?de~#f" ""","""abc?de~#f,<EOF>""",165))
    # def test_string_4(self):
    #     """test string"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "/* nguyen trung tinh */" ""","""/* nguyen trung tinh */,<EOF>""",166))
    # def test_string_5(self):
    #     """test string"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "//abcdef" ""","""//abcdef,<EOF>""",167))
    # def test_string_6(self):
    #     """test string"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "abc\\\\abc" ""","""abc\\\\abc,<EOF>""",168))
    # def test_string_7(self):
    #     """test string"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "abc\\babc\\fabc\\tabc" ""","""abc\\babc\\fabc\\tabc,<EOF>""",169))
    # def test_string_8(self):
    #     """test string"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "\\\\\\fabc\\\\rabc" ""","""\\\\\\fabc\\\\rabc,<EOF>""",170))
    # def test_string_9(self):
    #     """test string"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "abc\\tabc\\fabc\\b" ""","""abc\\tabc\\fabc\\b,<EOF>""",171))
    # def test_string_10(self):
    #     """test string"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "abc\"abc\\\\" ""","""abc,abc,Error Token \\""",172))
    

    # def test_unclose_string_1(self):
    #     """test unclose string"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "123a\\n123 ""","""Unclosed String: 123a\\n123 """,173))
    # def test_unclose_string_2(self):
    #     """test unclose string"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "abc"abc" ""","""abc,abc,Unclosed String:  """,174))
    # def test_unclose_string_3(self):
    #     """test unclose string"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "abc\\" ""","""Unclosed String: abc\\" """,175))
    # def test_unclose_string_4(self):
    #     """test unclose string"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "abc\\rabc" ""","""abc\\rabc,<EOF>""",176))
    # def test_unclose_string_5(self):
    #     """test unclose string"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "abc\nabc" ""","""Unclosed String: abc""",177))

    # def test_illegal_escape_1(self):
    #     """test illegal escape"""
    #     self.assertTrue(TestLexer.checkLexeme(""" 123 "12\\t3\\am123" ""","""123,Illegal Escape In String: 12\\t3\\a""",178))
    # def test_illegal_escape_2(self):
    #     """test illegal escape"""
    #     self.assertTrue(TestLexer.checkLexeme(""" abc "abc\\a" abc ""","""abc,Illegal Escape In String: abc\\a""",179))
    # def test_illegal_escape_3(self):
    #     """test illegal escape"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "\\\\\\\\\\abc" ""","""Illegal Escape In String: \\\\\\\\\\a""",180))
    # def test_illegal_escape_4(self):
    #     """test illegal escape"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "abc\\\nabc" ""","""Illegal Escape In String: abc\\\n""",181))
    # def test_illegal_escape_5(self):
    #     """test illegal escape"""
    #     self.assertTrue(TestLexer.checkLexeme(""" abc\\n"abc 123" ""","""abc,Error Token \\""",182))

    # def test_all_lexer_1(self):
    #     """test all_lexer"""
    #     self.assertTrue(TestLexer.checkLexeme(""" int main () {}""","""int,main,(,),{,},<EOF>""",183))
    # def test_all_lexer_2(self):
    #     """test all_lexer"""
    #     self.assertTrue(TestLexer.checkLexeme(""" int a[10]; ""","""int,a,[,10,],;,<EOF>""",184))
    # def test_all_lexer_3(self):
    #     """test all_lexer"""
    #     self.assertTrue(TestLexer.checkLexeme(""" int[] foo(int a, int b) {} ""","""int,[,],foo,(,int,a,,,int,b,),{,},<EOF>""",185))
    # def test_all_lexer_4(self):
    #     """test all_lexer"""
    #     self.assertTrue(TestLexer.checkLexeme(""" foo(2)[3+x]=20 ""","""foo,(,2,),[,3,+,x,],=,20,<EOF>""",186))
    # def test_all_lexer_5(self):
    #     """test all_lexer"""
    #     self.assertTrue(TestLexer.checkLexeme(""" /* this is a comment */ void foo() {if (a==0) {b = a+c}} """
    #     ,"""void,foo,(,),{,if,(,a,==,0,),{,b,=,a,+,c,},},<EOF>""",187))
    # def test_all_lexer_6(self):
    #     """test all_lexer"""
    #     self.assertTrue(TestLexer.checkLexeme(""" int i,j,k,a=5; ""","""int,i,,,j,,,k,,,a,=,5,;,<EOF>""",188))
    # def test_all_lexer_7(self):
    #     """test all_lexer"""
    #     self.assertTrue(TestLexer.checkLexeme(""" (5 || 8)[2] ""","""(,5,||,8,),[,2,],<EOF>""",189))
    # def test_all_lexer_8(self):
    #     """test all_lexer"""
    #     self.assertTrue(TestLexer.checkLexeme(""" abc + 1.e-8 = c ""","""abc,+,1.e-8,=,c,<EOF>""",190))
    # def test_all_lexer_9(self):
    #     """test all_lexer"""
    #     self.assertTrue(TestLexer.checkLexeme(""" string a; a = "nguyen trung tinh" ""","""string,a,;,a,=,nguyen trung tinh,<EOF>""",191))
    # def test_all_lexer_10(self):
    #     """test all_lexer"""
    #     self.assertTrue(TestLexer.checkLexeme(""" boolean b; b = true; ""","""boolean,b,;,b,=,true,;,<EOF>""",192))
    # def test_all_lexer_11(self):
    #     """test all_lexer"""
    #     self.assertTrue(TestLexer.checkLexeme(""" do {s = "nguyen trung tinh";} while (a < b); ""","""do,{,s,=,nguyen trung tinh,;,},while,(,a,<,b,),;,<EOF>""",193))
    # def test_all_lexer_12(self):
    #     """test all_lexer"""
    #     self.assertTrue(TestLexer.checkLexeme(""" int main( {} ""","""int,main,(,{,},<EOF>""",194))
    # def test_all_lexer_13(self):
    #     """test all_lexer"""
    #     self.assertTrue(TestLexer.checkLexeme(""" a + b < c <= d || e && f ""","""a,+,b,<,c,<=,d,||,e,&&,f,<EOF>""",195))
    # def test_all_lexer_14(self):
    #     """test all_lexer"""
    #     self.assertTrue(TestLexer.checkLexeme(""" 125/*58 ""","""125,/,*,58,<EOF>""",196))
    # def test_all_lexer_15(self):
    #     """test all_lexer"""
    #     self.assertTrue(TestLexer.checkLexeme(""" {abc(abc(*abc*)} ""","""{,abc,(,abc,(,*,abc,*,),},<EOF>""",197))
    # def test_all_lexer_16(self):
    #     """test all_lexer"""
    #     self.assertTrue(TestLexer.checkLexeme(""" /* !@#$%^& */ ""","""<EOF>""",198))
    # def test_all_lexer_17(self):
    #     """test all_lexer"""
    #     self.assertTrue(TestLexer.checkLexeme(""" 1.e5987^12 ""","""1.e5987,Error Token ^""",199))
    # def test_all_lexer_18(self):
    #     """test all_lexer"""
    #     self.assertTrue(TestLexer.checkLexeme(""" int a[[5]] ""","""int,a,[,[,5,],],<EOF>""",200))
