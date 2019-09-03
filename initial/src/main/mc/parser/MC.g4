grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::member {
def emit(self):
    tk = self.type
    if tk == UNCLOSE_STRING:       
        result = super.emit();
        raise UncloseString(result.text);
    elif tk == ILLEGAL_ESCAPE:
        result = super.emit();
        raise IllegalEscape(result.text);
    elif tk == ERROR_CHAR:
        result = super.emit();
        raise ErrorToken(result.text); 
    else:
        return super.emit();
}

options{
	language=Python3;
}



program  : mctype 'main' LB RB LP body? RP EOF ;//parser

mctype: INTTYPE | VOIDTYPE ;

body: funcall SEMI;

exp: funcall | INTLIT ;

funcall: ID LB exp? RB ;//
/*lexer*/ 
INTTYPE: 'int' ;

VOIDTYPE: 'void' ;

//keyword


ID: [a-zA-Z]+ ;
//indentifer
INTLIT: [0-9]+;

//literal

//oprerator

ADD:'+';
MUL:'*';
LOGN:'!';
LOGO:'||';
NOTE:'!=';
LT:'<';
LTOE:'<=';
ASSIG:'=';
SUB:'-';
DIV:'/';
MOD:'%';
LOGA:'&&';
EQ:'==';
GT:'>';
GTOE:'>=';

//separator
LSB:'[';
RSB:']';
LB: '(' ;

RB: ')' ;

LP: '{';

RP: '}';

SEMI: ';' ;

CM:',';

//cmt and space 
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;