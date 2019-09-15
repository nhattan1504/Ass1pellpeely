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



program  : manydecls +EOF;
manydecls: decl declTail;
declTail: decl (declTail)?;
decl: declVar|declfunc;
declVar:singleDeclvar|listDeclvar;
singleDeclvar:PrimiType (ID|ARRAYTYPE) SEMI;
listDeclvar: PrimiType listid SEMI;
listid: (ID|ARRAYTYPE) idtail;
idtail: CM (ID|ARRAYTYPE) idtail?;
declfunc: (PrimiType|ARRAYPTTYPE|VOIDTYPE) ID LB paralist RB blkStmt ;
paralist: para paratail?;
paratail: CM para paratail?;
para: (ID|ARRAYTYPE) listid;

//Expression
exp:;
expInt:;
expBl:;
expStmt:;

//Statements

ifStmt: IF LB EXPBL RB SMT (ELSE SMT)?  ;
forStmt: FOR LB EXPINT SEMI EXPBL SEMI EXPINT RB blkStmt ;
breakStmt :'break' SEMI;
continueStmt:'continue' SEMI;
doWhileStmt:DO SMT WHILE EXP;

blkStmt:LSB blkList RSB;
blkList: blk blkTail;
blkTail:  blkTail? ;
blk:declVar|stmt;
stmt:ifStmt|forStmt|breakStmt|doWhileStmt|expStmt|blkStmt ;





//
/*lexer*/ 
PrimiType:INTTYPE|BOOLEAN|FLOATTYPE|STRING;
INTTYPE: 'int' ;
BOOLEAN:'boolean';
VOIDTYPE: 'void' ;
FLOATTYPE:'float';
ARRAYTYPE:  ID LSB INTLIT RSB SEMI ;
ARRAYPTTYPE:Inparr|Outarr;
Inparr:(INTTYPE|BOOLEAN|FLOATTYPE) ID LSB RSB;
Outarr:(INTTYPE|BOOLEAN|FLOATTYPE) LSB RSB;
STRING:'A';
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