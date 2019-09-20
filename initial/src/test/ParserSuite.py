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
        expect = "Error on line 2 col 12: ;"
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
    def test_parser18(self):
        """Function declaration"""
        input = """
        void main()
        {
            do
            int a,b,c;
            a=b<c+d;
            while(d=3);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))
    def test_parser19(self):
        """Function declaration"""
        input = """
        void main()
        {
            break return a=b;
        }
        """
        expect = "Error on line 4 col 18: return"
        self.assertTrue(TestParser.checkParser(input,expect,219))
    def test_parser20(self):
        """Function declaration"""
        input = """
        void main()
        {
            break return a=b;
        }
        """
        expect = "Error on line 4 col 18: return"
        self.assertTrue(TestParser.checkParser(input,expect,220))
    def test_parser21(self):
        """Function declaration"""
        input = """
        int main(){
            a = b/c- d/ e*f;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))
    def test_parser22(self):
        """Function declaration"""
        input = """
        void main(){
            return a[10];
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))
    def test_parser23(self):
        """Function declaration"""
        input = """
        int main(){
        }
        void putInt(int f)
        {
            return 5;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))
    def test_parser24(self):
        """Function declaration"""
        input = """
        int main(){
            string abc;
           a==b=c;
           }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))
    def test_parser25(self):
        """Function declaration"""
        input = """
        void main(){
             321=_[123]+_[324]-_HAHHA;
           }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))
    def test_parser26(self):
        """Function declaration"""
        input = """
        void main(){
             check=check()[4[5]];
           }
        """
        expect = "Error on line 3 col 28: ["
        self.assertTrue(TestParser.checkParser(input,expect,226))
    def test_parser27(self):
        """Function declaration"""
        input = """
        void main(){
            strn= strings*10/checked(4)[a[1]];
           }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))
    def test_parser28(self):
        """Function declaration"""
        input = """
        void main(){
            strn= strings*10/checked(4)[a[1]];
           }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))
    def test_parser29(self):
        """Function declaration"""
        input = """
        int main()
        {
            for (i = 0; i < 10; i+1)
            {
                printf(i + 1);
                scanf("%d", a[i]);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))
    def test_parser30(self):
        """Function declaration"""
        input = """
        int main()
        {
            for (i = 0; i < 10; i+1)
            {
                printf("Nhap vao phan tu thu %d: ", i + 1);
                scanf("%d", &a[i]);
            }
        }
        """
        expect = "&"
        self.assertTrue(TestParser.checkParser(input,expect,230))
    def test_parser31(self):
        """Function declaration"""
        input = """
        void khoi_tao_queue()
        {
            front = rear = 0;
            queue_size = 0;
        }
        int is_empty()
        {
            return (queue_size == 0);
        }
        int is_full()
        {
	    return (queue_size == MAX);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))
    def test_parser32(self):
        """Function declaration"""
        input = """
        int main(float a, int b, string t){}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))
    def test_parser33(self):
        """Function declaration"""
        input = """
        int main(float a, int b, string t[]){}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))
    def test_parser34(self):
        """Function declaration"""
        input = """
        int main(float a, int b, string t[5]){}
        """
        expect = "Error on line 2 col 42: 5"
        self.assertTrue(TestParser.checkParser(input,expect,234))
    def test_parser35(self):
        """Function declaration"""
        input = """
       void foo ( float a[]) {}
                void goo (float x[]) {
                float y[10] ;
                int z[10] ;
                foo (x) ; 
                foo (y) ; 
                foo (z) ; 
                }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))
    def test_parser36(self):
        """Function declaration"""
        input = """
        float f = 1.23;
        """
        expect = "Error on line 2 col 16: ="
        self.assertTrue(TestParser.checkParser(input,expect,236))
    def test_parser37(self):
        """Function declaration"""
        input = """
         int main() {
            a[1][2];
        }
        """
        expect = "Error on line 3 col 16: ["
        self.assertTrue(TestParser.checkParser(input,expect,237))
    def test_parser38(self):
        """Function declaration"""
        input = """
         int main() {
            a = (b+ c) > d;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))
    def test_parser39(self):
        """Function declaration"""
        input = """
        int main() {
            foo(2)[3+x] = a[b[2]] +3;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,239))
    def test_parser40(self):
        """Function declaration"""
        input = """
           int[]foo(int b[]){
            int a [1];
            if (b>c) return a;
            else return b;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))
    def test_parser41(self):
        """Function declaration"""
        input = """
        int main() {
            if (a>3) a=4; else a<=3;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))
    def test_parser42(self):
        """Function declaration"""
        input = """
        int main() {
            do{
                a=1;
            }
            int a;
        }
        """
        expect = "Error on line 7 col 8: }"
        self.assertTrue(TestParser.checkParser(input,expect,242))
    def test_parser43(self):
        """Function declaration"""
        input = """
        int main() {
            i=1;
            100
            foo(1,2); 
        }
        """
        expect = "Error on line 5 col 12: foo"
        self.assertTrue(TestParser.checkParser(input,expect,243))
    def test_parser44(self):
        """Function declaration"""
        input = """
        int main() {
            int year;
            year = 2016;
            if (((year % 4 == 0) && (year % 100!= 0)) || (year%400 == 0))
            printf("%d la mot nam nhuan", year);
            else
            printf("%d khong phai la nam nhuan", year);
            return 0;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))
    def test_parser45(self):
        """Function declaration"""
        input = """
        int main() {
            int year;
            year = 2016;
            if (((year % 4 == 0) && (year % 100!= 0)) || (year%400 == 0))
            printf("%d la mot nam nhuan", year);
            else
            printf("%d khong phai la nam nhuan", year);
            return 0;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))
    def test_parser46(self):
        """Function declaration"""
        input = """
        int main()
        {
            printf("Hello World\\n");
            return 0;
            }
        
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))
    def test_parser47(self):
        """Function declaration"""
        input = """
        int main()
        {
            int c = 1;  
            do
            {
                printf("%d ", c);  
                c+1;
            }
            while (c <= 10)  
            return 0;
        }
        """
        expect = "Error on line 4 col 18: ="
        self.assertTrue(TestParser.checkParser(input,expect,247))
    def test_parser48(self):
        """Function declaration"""
        input = """
        int main()
        {
            int c;
            c=1;  
            do
            {
                printf("%d ", c);  
                c+1;
            }
            while (c <= 10);
            return 0;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))
    def test_parser49(self):
        """Function declaration"""
        input = """
        int main()
        {
        int array[100], n, c;
   
        printf("Enter number of elements in array\\n");
        scanf("%d", &n);
   
        printf("Enter %d elements\n", n);
   
        for (c = 0; c < n; c++)
        scanf("%d", &array[c]);
   
        printf("The array elements are:\n");
   
        for (c = 0; c < n; c++)
        printf("%d\n", array[c]);
   
        return 0;
        }
        }
        """
        expect = "&"
        self.assertTrue(TestParser.checkParser(input,expect,249))
    def test_parser50(self):
        """Function declaration"""
        input = """
        int main()
        {
        printf("Writing comments is very useful.\\n");
        printf("Good luck C programmer.\\n");
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,250))
    def test_parser51(self):
        """Function declaration"""
        input = """
        int main(){

        }
        {

        }
        """
        expect = "Error on line 5 col 8: {"
        self.assertTrue(TestParser.checkParser(input,expect,251))
    def test_parser52(self):
        """Function declaration"""
        input = """
        int main(){if(b) if (a) else {} else {} }
        """
        expect = "Error on line 2 col 32: else"
        self.assertTrue(TestParser.checkParser(input,expect,252))
    def test_parser53(self):
        """Function declaration"""
        input = """
        int main(){if(b) if (a) c+1; else {} else {} }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))
    def test_parser54(self):
        """Function declaration"""
        input = """
        void main()
        { 
            c+[a+b];
        }
        """
        expect = "Error on line 4 col 14: ["
        self.assertTrue(TestParser.checkParser(input,expect,254))
    def test_parser55(self):
        input = """
        int x,y;
        int main() {
            x+y;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))
    def test_parser56(self):
        input = """
        int checked(int n)
        {
            if(n%2==0)
            return true;
        }
        int main() {}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,256))
    def test_parser57(self):
        input = """
        int main()
        {
           break;
           return ;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))
    def test_parser58(self):
        input = """
        int main()
        {
            int a=100,b=200;
            C=2*(a+b);
            S=a*b;
        }
        """
        expect = "Error on line 4 col 17: ="
        self.assertTrue(TestParser.checkParser(input,expect,258))
    def test_parser59(self):
        input = """
        int main()
        {
            int a,b;
            a=100;
            b=200;
            c=2*(a+b);
            s=a*b;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,259))
    def test_parser60(self):
        input = """
        int main()
        {
            for(i;i;i=i+1)
            {

            }
            {

            }
            {

            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))
    def test_parser61(self):
        input = """
        int main()
        {
        int c;
 
        for (c = 1; c <= 10; c+1)
        printf("%d\\n", c);
   
        getch();
        return 0;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))
    def test_parser62(self):
        input = """
        int main()
        {
            if(check==true)
            printf("successful");
            return 0;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))
    def test_parser63(self):
        input = """
        int main()
        {
            if(a<=1 && b>=2)
            {
                continue
            }
            else
            {
                do{
                }
                while a==true;
            }
        }
        """
        expect = "Error on line 7 col 12: }"
        self.assertTrue(TestParser.checkParser(input,expect,263))
    def test_parser64(self):
        input = """
        int main()
        {
            if(a<=1 && b>=2)
            {
                continue;
            }
            else
            {
                do{
                }
                while a==true;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,264))
    def test_parser65(self):
        input = """
        int main()
        {
            do {
                int poor(){};
            }
            {
                a+b;
            }
            while (a<5);
        }
        """
        expect = "Error on line 5 col 24: ("
        self.assertTrue(TestParser.checkParser(input,expect,265))
    def test_parser66(self):
        input = """
        int main()
        {
            /* love you 3000 */
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,266))
    def test_parser67(self):
        input = """
        int main()
        {
            /* love you 3000 */
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,267))
    def test_parser68(self):
        input = """
        int main()
        {
            int num1, num2;  
            float fraction;     
            string character;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))
    def test_parser69(self):
        input = """
        int main()
        {
            if(number < 100)
            printf("Number is less than 100!\n");
            else if(number == 100)
            printf("Number is 100!\n");
        }
        """
        expect = "Number is less than 100!"
        self.assertTrue(TestParser.checkParser(input,expect,269))
    def test_parser70(self):
        input = """
        int main()
        {
           int number;
           number=foo(10,a[10]);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,270))
    def test_parser71(self):
        input = """
        int main()
        {
           int number;
           number=foo(10,a[10][]);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,271))
    def test_parser72(self):
        input = """
       int main(){
            int main()
                {
                }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,272))
    def test_parser73(self):
        input = """
       int main(){
            int main()
                {
                }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,273))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
     
    
    
    
    

