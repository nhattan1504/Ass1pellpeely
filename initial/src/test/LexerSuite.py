import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("boolean abc","boolean,abc,<EOF>",101))
        self.assertTrue(TestLexer.checkLexeme("aCBbdc","aCBbdc,<EOF>",102))
        self.assertTrue(TestLexer.checkLexeme("aABVN","aABVN,<EOF>",103))
    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("123a123","123,a,123,<EOF>",104))