grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::members {
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
}

options{
	language=Python3;
}



program  : decl+ EOF;
decl: declVar|declfunc;
declVar:primiType listid SEMI;
listid:var (CM var)*;
var: ID (LSB INTLIT RSB)?;

//decla func
declfunc: (primiType|outArr|VOIDTYPE) ID LB paralist? RB LP stmt* RP ;
paralist: para CM paralist|para;
para: primiType (ID| ID LSB RSB) ;

BOOLIT:TRUE|FALSE;

//Expression

exp:expLo ASSIG exp|expLo;
expLo:expLo LOGO expAn|expAn;
expAn:expAn LOGA expEq|expEq;
expEq:expLogic (EQ|NOTE) expLogic|expLogic;
expLogic: expAs (LT|LTOE|GT|GTOE) expAs|expAs;
expAs:expAs(ADD|SUB) expDmm|expDmm;
expDmm:expDmm(DIV|MUL|MOD) expUna|expUna;
expUna:(SUB|LOGN) expV|expV;
expV: index|expH  ;
expH: LB exp RB |op;
index:funcall LSB exp RSB | ID LSB exp RSB;
invo:ID LB list_exp? RB;
list_exp:exp (CM exp)*;
op:INTLIT|FLOATLIT|STRINGLIT|BOOLIT|ID|invo ;




expStmt:exp SEMI;



funcall:ID LB list_exp? RB ;
//Statements

ifStmt: IF LB exp RB stmt(ELSE stmt)? ;

forStmt: FOR LB exp SEMI exp SEMI exp RB stmt ;

breakStmt :BREAK SEMI;

continueStmt:CONTINUE SEMI;

doWhileStmt:DO  stmt+  WHILE exp SEMI;


blkStmt:LP stmt* RP;

retNon:RETURN SEMI;
retExp: RETURN exp SEMI;
retStmt: retNon|retExp;


stmt:ifStmt|forStmt|breakStmt|doWhileStmt|expStmt|blkStmt|retStmt|continueStmt|expStmt |declVar  ;





//
/*lexer*/ 
primiType:INTTYPE|BOOLEAN|FLOATTYPE|STRINGTYPE;
INTTYPE: 'int' ;
BOOLEAN:'boolean';
VOIDTYPE: 'void' ;
FLOATTYPE:'float';
arrayType:  ID LSB exp RSB  ;
arrayPtType:inpArr|outArr;
inpArr:primiType ID LSB RSB;
outArr:primiType LSB RSB;




//keyword

FOR:'for';
IF:'if';
ELSE:'else';
RETURN:'return';
WHILE:'while';
VOID:VOIDTYPE;
DO:'do';
TRUE:'true';
FALSE:'false';
STRINGTYPE:'string';
BREAK:'break';
CONTINUE:'continue';




//identified

ID: Letter LetterOrDigit*;
fragment Letter         :       [a-zA-Z_];
fragment LetterOrDigit  :       [0-9a-zA-Z_];
//literal

INTLIT: [0-9]+;

FLOATLIT: 	NUMPART DECPART? | INTLIT DECPART;
fragment NUMPART: INTLIT '.' | '.' INTLIT | INTLIT '.' INTLIT;
fragment DECPART: [Ee] SUB? INTLIT;

STRINGLIT:'"' Strings?'"'{self.text=self.text.strip('"')};
fragment Strings: String+;
fragment String:~["\r\n\\]|Escape;
fragment Escape:'\\'[bfrnt"'\\];




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
LINECMT:'//'(~[\r\n])*  -> skip;


UNCLOSE_STRING: '"' Strings?(EOF | [\r\n]) {self.text=self.text.lstrip('"').rstrip("\n\r")}; //ket thuc chuoi "
ILLEGAL_ESCAPE: '"' Strings?('\\' ~[bfrnt"\\]){self.text=self.text.lstrip('"')};// tra ve token nay vs nhung ki tu k hop le nhu \u 
ERROR_CHAR: .;// ki tu loi