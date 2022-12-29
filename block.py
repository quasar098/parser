

class Block:
    def __init__(self):
        self.statements = []

    def show(self):
        return {"statements": self.statements}

    def __repr__(self):
        spacer = "  "
        nl = "\n"

        def recurs(obj=None, c=0):
            name = type(obj).__name__
            total = f"<{name}(\n"
            try:
                s = obj.show()
            except AttributeError:
                if isinstance(obj, int):
                    return str(obj)
                if isinstance(obj, str):
                    return f"\"{obj}\""
                if isinstance(obj, list):
                    combo = f"{nl}{spacer*(c+1)}"
                    return f"[{combo}{f'{combo}'.join([recurs(_,c+1) for _ in obj])}{nl}{spacer*c}]"
                s = {}
            for shown in s:
                total += f"{spacer*(c+1)}{shown}={recurs(s[shown], c+1)}{nl}"
            return total + f"{spacer*c})>"
        return recurs(self)
