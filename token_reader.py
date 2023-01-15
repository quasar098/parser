from token import Token, TokenType, NoToken


class TokenReader:
    def __init__(self, tokens: list[Token]):
        self.mark = 0
        self.tokens = tokens

    def peek_token(self):
        if self.mark < 0:
            return None
        if len(self.tokens) <= self.mark:
            return None
        return self.tokens[self.mark]

    def _next_token(self):
        _ = self.peek_token()
        if _ is None:
            return NoToken()
        self.mark += 1
        return _

    def try_eat_many(self, t):
        times = 0
        while self.try_eat(t):
            times += 1
        return times

    def try_eat(self, t):
        if self.nt(t):
            return True
        return False

    def nt(self, *t: TokenType):
        """Check if the next Token is one of the specific TokenTypes"""
        for _ in t:
            if (tk := self._next_token()).type == _:
                return tk
            self.mark -= 1
        return NoToken()

    def nc(self, *c: str) -> bool:
        """Check if the next Token has a specific content"""
        return self._next_token().content == c

    def __repr__(self):
        return f"<TokenReader(mark={self.mark})>"
