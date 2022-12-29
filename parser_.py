from block import Block
from statements import *
from expressions import *
from token_reader import TokenReader
from token import Token, TokenType


# noinspection PyUnboundLocalVariable
class Parser:
    def __init__(self, tokens):
        tokens.append(Token(TokenType.NL, ""))
        self.reader = TokenReader(tokens)
        self.block = Block()

    def do(self) -> Block:
        while self.reader.peek_token() is not None:
            before_mark = self.reader.mark
            if self.reader.peek_token().type == TokenType.NL:
                self.reader.nt(TokenType.NL)
                continue
            if stmt := (self.declare_statement() or self.func_call_statement()):
                self.block.statements.append(stmt)
            if before_mark == self.reader.mark:
                raise NotImplementedError("the mark didn't change")
        return self.block

    def declare_statement(self):
        current = self.reader.mark
        if self.reader.nt(TokenType.DECL) \
                and (var := self.identifier_expr()) \
                and self.reader.nt(TokenType.EQUALS) \
                and (expr := self.expr()) \
                and self.reader.nt(TokenType.NL):
            return DeclareStatement(var, expr)
        self.reader.mark = current

    def func_call_statement(self):
        current = self.reader.mark
        if (var := self.identifier_expr()) \
                and self.reader.nt(TokenType.LPAR) \
                and (expr := self.expr()) \
                and self.reader.nt(TokenType.RPAR) \
                and self.reader.nt(TokenType.NL):
            return FuncCallStatement(var, [expr])
        self.reader.mark = current

    def atom(self):
        current = self.reader.mark
        if expr := (self.identifier_expr() or self.integer_expr() or self.string_expr()):
            return expr
        self.reader.mark = current

    def expr(self):
        current = self.reader.mark
        if sumexpr := self.sum_expr():
            return sumexpr
        self.reader.mark = current

    def sum_expr(self):
        def add_sum(left_):
            current_ = self.reader.mark
            if self.reader.nt(TokenType.PLUS) and (right_ := self.sum_expr()):
                return SumExpr(left_, right_)
            self.reader.mark = current_
            return left_

        current = self.reader.mark
        if mulexpr := self.mul_expr():
            return add_sum(mulexpr)
        self.reader.mark = current

    def mul_expr(self):
        def mul(left_):
            current_ = self.reader.mark
            if self.reader.nt(TokenType.TIMES) and (right_ := self.mul_expr()):
                return MultiplyExpr(left_, right_)
            self.reader.mark = current_
            return left_

        current = self.reader.mark
        if atomexpr := self.atom():
            return mul(atomexpr)
        self.reader.mark = current

    def string_expr(self):
        current = self.reader.mark
        if expr := self.reader.nt(TokenType.STRING):
            return StringExpr(expr.content)
        self.reader.mark = current

    def integer_expr(self):
        current = self.reader.mark
        if expr := self.reader.nt(TokenType.INTEGER):
            return IntegerExpr(int(expr.content))
        self.reader.mark = current

    def identifier_expr(self):
        current = self.reader.mark
        if expr := self.reader.nt(TokenType.IDENTIFIER):
            return IdentifierExpr(expr.content)
        self.reader.mark = current
