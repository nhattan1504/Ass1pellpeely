import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

    def test_parser1(self):
        """Simple program: int main() {} """
        input = """int main() {
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    def test_parser2(self):
        """Simple program: int main() {} """
        input = """int main() {
            ;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    def test_parser3(self):
        """Simple program: int main() {} """
        input = """int main() {
            
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,203))
    def test_parser4(self):
        """Simple program: int main() {} """
        input = """int main() {
            return ;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    def test_parser5(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,bc
            }
        """
        expect = "Error on line 3 col 12: }"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    def test_parser6(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b,c;
            }
            int a;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))
    def test_parser7(self):
        """Simple program: int main() {} """
        input = """int main() {
            int a,b,c[3];
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207)) 
    def test_parser8(self):
        """Simple program: int main() {} """
        input = """
        int a,b,c[5];
        string str;
        boolean boo;
        float f;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208)) 
    def test_parser9(self):
        """Simple program: int main() {} """
        input = """
        void main(){
            do{
                string str;
                str = "true";
            }while(true)
        }
        """
        expect = "Error on line 7 col 8: }"
        self.assertTrue(TestParser.checkParser(input,expect,209)) 
    def test_parser10(self):
        """Simple program: int main() {} """
        input = """
        void main(){
            do{
                string str;
                str = "true";
            }while(true);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210)) 
    def test_parser11(self):
        """Simple program: int main() {} """
        input = """
        int main(){
            for(i;a;b)
            {
                string str;
                str = "true";
            }
            
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211)) 
    def test_parser12(self):
        """Simple program: int main() {} """
        input = """
        int main(){
            {
                //comment
            }
            {
                funcall1(a,b);
            }
            {
                str = "string";
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212)) 
    def test_parser13(self):
        """Simple program: int main() {} """
        input = """
        int main(){
            {
             return a;  
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))
    def test_parser14(self):
        """Simple program: int main() {} """
        input = """
        int main(){
            {
               
            }
            return &;
        }
        """
        expect = "&"
        self.assertTrue(TestParser.checkParser(input,expect,214))
    def test_parser15(self):
        """Simple program: int main() {} """
        input = """
        int main() {
            if(a>b){
        }
        """
        expect = "Error on line 5 col 8: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,215))
    def test_parser16(self):
        """Simple program: int main() {} """
        input = """
        int main()
        {
            func(2,3)(4);
        }
        """
        expect = "Error on line 4 col 21: ("
        self.assertTrue(TestParser.checkParser(input,expect,216))
    def test_parser17(self):
        """Function declaration"""
        input = """
        void foo(int x);
        """
        expect = "Error on line 2 col 23: ;"
        self.assertTrue(TestParser.checkParser(input,expect,217))

    
    
    
    
    
     
    
    
    
    

