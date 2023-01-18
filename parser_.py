from block import Block
from expressions import *
from statements import *
from token import TokenType
from token_reader import TokenReader


# noinspection PyUnboundLocalVariable
class Parser:
    def __init__(self, tokens):
        self.reader = TokenReader(tokens)

    def do(self) -> Block:
        return self.block()

    def statement(self):
        if stmt := (self.declare_statement() or self.declare_function_statement() or self.operator_and_equals_statement()
                    or self.if_statement() or self.func_call_statement()):
            return stmt

    def declare_statement(self):
        current = self.reader.mark
        if (var := self.identifier_expr()) \
                and self.reader.nt(TokenType.EQUALS) \
                and (expr := self.expr()):
            return DeclareStatement(var, expr)
        self.reader.mark = current

    def declare_function_statement(self):
        current = self.reader.mark
        if (var := self.identifier_expr()) \
                and self.reader.nt(TokenType.COLON) \
                and self.reader.nt(TokenType.EQUALS) and self.reader.nt(TokenType.LCURLY) \
                and (block := self.block()) and self.reader.nt(TokenType.RCURLY):
            return DeclareFunctionStatement(var, block)
        self.reader.mark = current

    def operator_and_equals_statement(self):
        """+=, -=, *=, /="""
        current = self.reader.mark
        if (var := self.identifier_expr()) \
                and (oper := self.reader.nt(TokenType.PLUS, TokenType.MINUS, TokenType.TIMES, TokenType.SLASH)) \
                and self.reader.nt(TokenType.EQUALS) \
                and (expr := self.expr()):
            return DeclareStatement(var, {
                TokenType.PLUS: SumExpr,
                TokenType.MINUS: SubExpr,
                TokenType.TIMES: MultiplyExpr,
                TokenType.SLASH: DivideExpr
            }[oper.type](var, expr))
        self.reader.mark = current

    def block(self):
        stmts = []
        self.reader.try_eat_many(TokenType.NL)
        current = self.reader.mark
        while self.reader.peek_token() is not None and (stmt := self.statement()) \
                and self.reader.try_eat_many(TokenType.NL):
            current = self.reader.mark
            stmts.append(stmt)
        self.reader.mark = current
        if stmt := self.statement():
            stmts.append(stmt)
        else:
            self.reader.mark = current
        return Block(stmts)

    def func_call_statement(self):
        current = self.reader.mark
        if expr := self.call_expr():
            return FuncCallStatement(expr)
        self.reader.mark = current

    def if_statement(self):
        current = self.reader.mark
        if self.reader.nt(TokenType.IF) and self.reader.nt(TokenType.LPAR) \
                and (cond := self.expr()) and self.reader.nt(TokenType.RPAR) \
                and self.reader.nt(TokenType.LCURLY) \
                and (block := self.block()) and self.reader.nt(TokenType.RCURLY):
            return IfStatement(cond, block)
        self.reader.mark = current

    def atom(self):
        current = self.reader.mark
        if expr := (self.identifier_expr() or self.integer_expr() or self.string_expr()
                    or self.true_expr() or self.false_expr()):
            return expr
        self.reader.mark = current

    def true_expr(self):
        current = self.reader.mark
        if self.reader.nt(TokenType.TRUE):
            return TrueExpr()
        self.reader.mark = current

    def false_expr(self):
        current = self.reader.mark
        if self.reader.nt(TokenType.FALSE):
            return FalseExpr()
        self.reader.mark = current

    def expr(self):
        current = self.reader.mark
        if sumexpr := self.or_expr():
            return sumexpr
        self.reader.mark = current

    def or_expr(self):
        def try_or(left_):
            current_ = self.reader.mark
            if self.reader.nt(TokenType.PIPE) and self.reader.nt(TokenType.PIPE) and (right_ := self.equals_expr()):
                return try_or(ComparisonOrExpr(left_, right_))
            self.reader.mark = current_
            return left_

        current = self.reader.mark
        if eqexpr := self.equals_expr():
            return try_or(eqexpr)
        self.reader.mark = current

    def equals_expr(self):
        def try_equals(left_):
            current_ = self.reader.mark
            if self.reader.nt(TokenType.EQUALS) and self.reader.nt(TokenType.EQUALS) and \
                    (right_ := self.greater_or_less_than_expr()):
                return try_equals(ComparisonEqualsExpr(left_, right_))
            self.reader.mark = current_
            return left_

        current = self.reader.mark
        if golexpr := self.greater_or_less_than_expr():
            return try_equals(golexpr)
        self.reader.mark = current

    def greater_or_less_than_expr(self):
        def try_compare(left_):
            current_ = self.reader.mark
            if self.reader.nt(TokenType.RANGLE) and (right_ := self.sum_expr()):
                return try_compare(ComparisonGreaterThanExpr(left_, right_))
            self.reader.mark = current_
            if self.reader.nt(TokenType.LANGLE) and (right_ := self.sum_expr()):
                return try_compare(ComparisonLessThanExpr(left_, right_))
            self.reader.mark = current_
            return left_

        current = self.reader.mark
        if sumexpr := self.sum_expr():
            return try_compare(sumexpr)
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
            exprs = []
            if self.reader.nt(TokenType.LPAR):
                current3 = self.reader.mark
                while (arg := self.expr()) and self.reader.nt(TokenType.COMMA):
                    current3 = self.reader.mark
                    exprs.append(arg)
                self.reader.mark = current3
                if arg := self.expr():
                    exprs.append(arg)
                else:
                    self.reader.mark = current3
                if self.reader.nt(TokenType.RPAR):
                    return FuncCallExpr(left_, exprs)
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
