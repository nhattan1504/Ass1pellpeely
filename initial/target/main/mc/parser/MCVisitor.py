# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MCParser import MCParser
else:
    from MCParser import MCParser

# This class defines a complete generic visitor for a parse tree produced by MCParser.

class MCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx:MCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#manydecls.
    def visitManydecls(self, ctx:MCParser.ManydeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#declTail.
    def visitDeclTail(self, ctx:MCParser.DeclTailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#decl.
    def visitDecl(self, ctx:MCParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#declVar.
    def visitDeclVar(self, ctx:MCParser.DeclVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#singleDeclvar.
    def visitSingleDeclvar(self, ctx:MCParser.SingleDeclvarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#listDeclvar.
    def visitListDeclvar(self, ctx:MCParser.ListDeclvarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#listid.
    def visitListid(self, ctx:MCParser.ListidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#idtail.
    def visitIdtail(self, ctx:MCParser.IdtailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#declfunc.
    def visitDeclfunc(self, ctx:MCParser.DeclfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#paralist.
    def visitParalist(self, ctx:MCParser.ParalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#paratail.
    def visitParatail(self, ctx:MCParser.ParatailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#para.
    def visitPara(self, ctx:MCParser.ParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp.
    def visitExp(self, ctx:MCParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expUna.
    def visitExpUna(self, ctx:MCParser.ExpUnaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expAssig.
    def visitExpAssig(self, ctx:MCParser.ExpAssigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expAS.
    def visitExpAS(self, ctx:MCParser.ExpASContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expLogic.
    def visitExpLogic(self, ctx:MCParser.ExpLogicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expEq.
    def visitExpEq(self, ctx:MCParser.ExpEqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expAn.
    def visitExpAn(self, ctx:MCParser.ExpAnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expLo.
    def visitExpLo(self, ctx:MCParser.ExpLoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expAssg.
    def visitExpAssg(self, ctx:MCParser.ExpAssgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#op.
    def visitOp(self, ctx:MCParser.OpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expStmt.
    def visitExpStmt(self, ctx:MCParser.ExpStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expList.
    def visitExpList(self, ctx:MCParser.ExpListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#ifStmt.
    def visitIfStmt(self, ctx:MCParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#forStmt.
    def visitForStmt(self, ctx:MCParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#breakStmt.
    def visitBreakStmt(self, ctx:MCParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#continueStmt.
    def visitContinueStmt(self, ctx:MCParser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#doWhileStmt.
    def visitDoWhileStmt(self, ctx:MCParser.DoWhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#listStmt.
    def visitListStmt(self, ctx:MCParser.ListStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#blkStmt.
    def visitBlkStmt(self, ctx:MCParser.BlkStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#blkList.
    def visitBlkList(self, ctx:MCParser.BlkListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#blk.
    def visitBlk(self, ctx:MCParser.BlkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#stmt.
    def visitStmt(self, ctx:MCParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#primiType.
    def visitPrimiType(self, ctx:MCParser.PrimiTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#arrayType.
    def visitArrayType(self, ctx:MCParser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#arrayPtType.
    def visitArrayPtType(self, ctx:MCParser.ArrayPtTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#inpArr.
    def visitInpArr(self, ctx:MCParser.InpArrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#outArr.
    def visitOutArr(self, ctx:MCParser.OutArrContext):
        return self.visitChildren(ctx)



del MCParser