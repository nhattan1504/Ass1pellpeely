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



program  : partdec +EOF;
partdec: vardec | funcdec ;




//Expression
EXP:;
EXPINT:;
EXPBL:;
EXPSMT:;

//Statements
SMT:IFSMT|FORSMT|BREAKSt|DOWHILESMT|EXPSMT;
IFSMT: IF LB EXPBL RB SMT (ELSE SMT)?  ;
FORSMT: FOR LB EXPINT SEMI EXPBL SEMI EXPINT RB ;
BREAKSt :'break' SEMI;
CONTINUESt:'continue' SEMI;
DOWHILESMT:DO SMT WHILE EXP;





//
/*lexer*/ 
INTTYPE: 'int' ;
BOOLEAN:'boolean';
VOIDTYPE: 'void' ;
FLOATTYPE:'float';
ARRAYTYPE: (INTTYPE|BOOLEAN|FLOATTYPE) ID LSB INTLIT RSB SEMI ;
ARRAYPTTYPE:Inparr|Outarr;
Inparr:(INTTYPE|BOOLEAN|FLOATTYPE) ID LSB RSB;
Outarr:(INTTYPE|BOOLEAN|FLOATTYPE) LSB RSB;
//keyword

FOR:'for';
IF:'if';
THEN:'then';
ELSE:'else';
RETURN:'return';
WHILE:'while';
VOID:VOIDTYPE;
DO:'do';
TRUE:'true';
FALSE:'false';


//identified
ID: Letter LetterOrDigit*;
fragment Letter         :       [a-zA-Z_];
fragment LetterOrDigit  :       [0-9a-zA-Z_];
//literal

INTLIT: [0-9]+;

FLOATLIT: 	NUMPART DECPART? | INTLIT DECPART;
fragment NUMPART: INTLIT '.' | '.' INTLIT | INTLIT '.' INTLIT;
fragment DECPART: [Ee] SUB? INTLIT;

BOOLIT:TRUE|FALSE;



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
BLOCKCMT:'/*' .*? '*/' ->skip;
LINECMT:'//' .*? -> skip;

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;