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



program  : manydecls+ EOF;
manydecls: decl declTail;
declTail: (decl declTail)?;
decl: declVar|declfunc;
declVar:singleDeclvar|listDeclvar;
singleDeclvar:primiType (ID SEMI|arrayType) ;
listDeclvar: primiType listid SEMI;
listid: (ID|arrayType) idtail;
idtail: CM (ID|arrayType) idtail?;
declfunc: (primiType|arrayPtType|VOIDTYPE) ID LB paralist? RB blkStmt ;
paralist: para paratail;
paratail: CM para paratail?;
para: (ID|arrayType) listid;

//Expression
exp: expUna LSB RSB |expUna ;
expUna:(SUB|LOGN) expUna|expAssig;
expAssig: expAssig (DIV|MUL|MOD) expAS| expAS ;
expAS: expAS (ADD|SUB) expLogic|expLogic ;
expLogic: expEq (LT|LTOE|GT|GTOE) expEq|expEq ;
expEq:expAn (EQ|NOTE) expAn|expAn;
expAn:expAn LOGA expLo | expLo;
expLo:expLo LOGO expAssg|expAssg;
expAssg: op ASSIG expAssg | op;
op: INTLIT|FLOATLIT|STRINGLIT|ID|LP exp RP;
expStmt:expList SEMI;
expList: exp expList|exp ;

//Statements

ifStmt: IF LB exp RB stmt (ELSE stmt)?  ;
forStmt: FOR LB INTTYPE ID exp SEMI exp SEMI exp RB blkStmt? ;
breakStmt :'break' SEMI;
continueStmt:'continue' SEMI;
doWhileStmt:DO  (listStmt|(LB listStmt RB)) SEMI WHILE exp;
listStmt: stmt listStmt| stmt;
blkStmt:LP blkList? RP;
blkList: blk blkList|blk;
blk:declVar|stmt;
stmt:ifStmt|forStmt|breakStmt|doWhileStmt|expStmt|blkStmt ;

//con thieu line stmt



//
/*lexer*/ 
primiType:INTTYPE|BOOLEAN|FLOATTYPE|STRING;
INTTYPE: 'int' ;
BOOLEAN:'boolean';
VOIDTYPE: 'void' ;
FLOATTYPE:'float';
arrayType:  ID LSB INTLIT RSB SEMI ;
arrayPtType:inpArr|outArr;
inpArr:(INTTYPE|BOOLEAN|FLOATTYPE) ID LSB RSB;
outArr:(INTTYPE|BOOLEAN|FLOATTYPE) LSB RSB;
STRING:'string';
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

STRINGLIT:'"' Strings?'"'{self.text=self.text.strip('"')};
fragment Strings: String+;
fragment String:~["\r\n\\]|Escape;
fragment Escape:'\\'[bfrnt"'\\];
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


UNCLOSE_STRING: '"' Strings?(EOF | [\r\n]) {self.text=self.text.lstrip('"').rstrip("\n\r")}; //ket thuc chuoi "
ILLEGAL_ESCAPE: '"' Strings?('\\' ~[bfrnt"\\]){self.text=self.text.lstrip('"')};// tra ve token nay vs nhung ki tu k hop le nhu \u 
ERROR_CHAR: .;// ki tu loi