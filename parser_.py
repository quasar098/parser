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
            if stmt := self.statement():
                self.block.statements.append(stmt)
            if before_mark == self.reader.mark:
                raise NotImplementedError("the mark didn't change")
        return self.block

    def statement(self):
        current = self.reader.mark
        if stmt := (self.declare_statement() or self.declare_lambda_statement()
                    or self.func_call_statement() or self.if_statement()):
            return stmt
        self.reader.mark = current

    def declare_statement(self):
        current = self.reader.mark
        if self.reader.nt(TokenType.DECL) \
                and (var := self.identifier_expr()) \
                and self.reader.nt(TokenType.EQUALS) \
                and (expr := self.expr()) \
                and self.reader.nt(TokenType.NL):
            return DeclareStatement(var, expr)
        self.reader.mark = current

    def declare_lambda_statement(self):
        current = self.reader.mark
        if self.reader.nt(TokenType.FUNC) \
                and (var := self.identifier_expr()) \
                and self.reader.nt(TokenType.COLON) \
                and self.reader.nt(TokenType.EQUALS) \
                and (expr := self.expr()) \
                and self.reader.nt(TokenType.NL):
            return DeclareLambdaStatement(var, expr)
        self.reader.mark = current

    def get_block(self):
        current = self.reader.mark
        if self.reader.nt(TokenType.LCURLY):
            self.reader.try_eat(TokenType.NL)
            b = Block()
            while True:
                current2 = self.reader.mark
                if stmt := self.statement():
                    b.statements.append(stmt)
                else:
                    self.reader.mark = current2
                    break
            if self.reader.nt(TokenType.RCURLY):
                return b
        self.reader.mark = current

    def func_call_statement(self):
        current = self.reader.mark
        if (expr := self.call_expr()) and self.reader.nt(TokenType.NL):
            return FuncCallStatement(expr)
        self.reader.mark = current

    def if_statement(self):
        current = self.reader.mark
        if self.reader.nt(TokenType.IF) and self.reader.nt(TokenType.LPAR) \
                and (cond := self.expr()) and self.reader.nt(TokenType.RPAR) \
                and (block := self.get_block()) and self.reader.nt(TokenType.NL):
            return IfStatement(cond, block)
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
            if self.reader.nt(TokenType.PLUS) and (right_ := self.sub_expr()):
                return add_sum(SumExpr(left_, right_))
            self.reader.mark = current_
            return left_

        current = self.reader.mark
        if subexpr := self.sub_expr():
            return add_sum(subexpr)
        self.reader.mark = current

    def sub_expr(self):
        def sub(left_):
            current_ = self.reader.mark
            if self.reader.nt(TokenType.MINUS) and (right_ := self.mul_expr()):
                return sub(SubExpr(left_, right_))
            self.reader.mark = current_
            return left_

        current = self.reader.mark
        if mulexpr := self.mul_expr():
            return sub(mulexpr)
        self.reader.mark = current

    def mul_expr(self):
        def mul(left_):
            current_ = self.reader.mark
            if self.reader.nt(TokenType.TIMES) and (right_ := self.div_expr()):
                return mul(MultiplyExpr(left_, right_))
            self.reader.mark = current_
            return left_

        current = self.reader.mark
        if divexpr := self.div_expr():
            return mul(divexpr)
        self.reader.mark = current

    def div_expr(self):
        def div(left_):
            current_ = self.reader.mark
            if self.reader.nt(TokenType.SLASH) and (right_ := self.unary_minus_expr()):
                return div(DivideExpr(left_, right_))
            self.reader.mark = current_
            return left_

        current = self.reader.mark
        if umexpr := self.unary_minus_expr():
            return div(umexpr)
        self.reader.mark = current

    def unary_minus_expr(self):
        current = self.reader.mark
        if cexpr := self.call_expr():
            return cexpr
        self.reader.mark = current

        current = self.reader.mark
        if self.reader.nt(TokenType.MINUS) and (cexpr := self.call_expr()):
            return UnaryMinusExpr(cexpr)
        self.reader.mark = current

    def call_expr(self):
        def trycall(left_):
            current_ = self.reader.mark
            if self.reader.nt(TokenType.LPAR):
                current3 = self.reader.mark
                if (arg := self.expr()) and self.reader.nt(TokenType.RPAR):
                    return FuncCallExpr(left_, [arg])
                self.reader.mark = current3
                if self.reader.nt(TokenType.RPAR):
                    return FuncCallExpr(left_, [])
            self.reader.mark = current_
            return left_

        current = self.reader.mark
        if atomexpr := self.atom():
            return trycall(atomexpr)
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
