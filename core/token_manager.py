# core/token_manager.py

class TokenManager:
    def __init__(self):
        self.tokens = []  # Liste de tuples (représentation_visuelle, code_interne)

    def add_token(self, visual, internal):
        self.tokens.append((visual, internal))

    def pop_token(self):
        if self.tokens:
            return self.tokens.pop()
        return None

    def clear(self):
        self.tokens.clear()

    def get_visual_expression(self):
        if not self.tokens:
            return "0"
        return "".join(t[0] for t in self.tokens)

    def get_internal_expression(self):
        if not self.tokens:
            return "0"
        return "".join(t[1] for t in self.tokens)