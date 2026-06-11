# core/calculator_engine.py

import math
from core.token_manager import TokenManager
from core.scientific_functions import ScientificFunctions
from core.memory_manager import MemoryManager

class CalculatorEngine:
    def __init__(self):
        self.token_manager = TokenManager()
        self.scientific = ScientificFunctions()
        self.memory = MemoryManager()
        self.is_second_active = False
        self.angle_mode = "Rad"

    def toggle_second(self):
        self.is_second_active = not self.is_second_active
        return self.is_second_active

    def toggle_angle_mode(self):
        self.angle_mode = "Deg" if self.angle_mode == "Rad" else "Rad"
        self.scientific.set_angle_mode(self.angle_mode)
        return self.angle_mode

    def clear_entry(self):
        self.token_manager.clear()

    def delete_last(self):
        self.token_manager.pop_token()

    def add_input(self, value):
        # Configuration des redirections de boutons vers les fonctions mathématiques internes
        mappings = {
            "π": ("π", "math.pi"),
            "e": ("e", "math.e"),
            "x²": ("²", "**2"),
            "x³": ("³", "**3"),
            "√x": ("√(", "math.sqrt("),
            "∛x": ("∛(", "self.scientific.cube_root("),
            "xʸ": ("^", "**"),
            "ʸ√x": ("^(1/", "**(1/"),
            "10ˣ": ("10^(", "10**("),
            "2ˣ": ("2^(", "2**("),
            "log": ("log10(", "math.log10("),
            "logᵧx": ("log_base(", "self.scientific.log_y("),
            "ln": ("ln(", "math.log("),
            "eˣ": ("e^(", "math.exp("),
            "sin": ("sin(", "self.scientific.sin("),
            "cos": ("cos(", "self.scientific.cos("),
            "tan": ("tan(", "self.scientific.tan("),
            "sin⁻¹": ("sin⁻¹(", "self.scientific.asin("),
            "cos⁻¹": ("cos⁻¹(", "self.scientific.acos("),
            "tan⁻¹": ("tan⁻¹(", "self.scientific.atan("),
            "sinh": ("sinh(", "self.scientific.sinh("),
            "cosh": ("cosh(", "self.scientific.cosh("),
            "tanh": ("tanh(", "self.scientific.tanh("),
            "sinh⁻¹": ("sinh⁻¹(", "self.scientific.asinh("),
            "cosh⁻¹": ("cosh⁻¹(", "self.scientific.acosh("),
            "tanh⁻¹": ("tanh⁻¹(", "self.scientific.atanh("),
            "|x|": ("abs(", "abs("),
            "1/x": ("1/(", "1/("),
            "n!": ("fact(", "self.scientific.factorial("),
            "exp": ("e+", "*10**"),
            "mod": (" mod ", "%"),
            "%": ("/100", "/100")
        }

        if value in mappings:
            visual, internal = mappings[value]
            self.token_manager.add_token(visual, internal)
        elif value == "+/-":
            self.token_manager.add_token("-", "-")
        else:
            self.token_manager.add_token(str(value), str(value))

    def handle_memory(self, action):
        if action == "MC":
            self.memory.clear()
        elif action == "MR":
            val = str(self.memory.recall())
            self.token_manager.add_token(val, val)
        else:
            try:
                expr = self.token_manager.get_internal_expression()
                current_val = float(eval(expr, {"__builtins__": None}, {"math": math, "self": self, "abs": abs}))
            except Exception:
                current_val = 0.0

            if action == "M+":
                self.memory.add(current_val)
            elif action == "M-":
                self.memory.subtract(current_val)
            elif action == "MS":
                self.memory.store(current_val)

    def evaluate(self):
        expr = self.token_manager.get_internal_expression()
        if not expr or expr == "0":
            return "0"

        # Fermeture automatique des parenthèses manquantes
        open_brackets = expr.count("(")
        close_brackets = expr.count(")")
        if open_brackets > close_brackets:
            expr += ")" * (open_brackets - close_brackets)

        try:
            context = {
                "math": math,
                "self": self,
                "abs": abs
            }
            res = eval(expr, {"__builtins__": None}, context)
            if isinstance(res, float):
                if res.is_integer():
                    res = int(res)
                else:
                    res = round(res, 10)

            str_res = str(res)
            self.token_manager.clear()
            self.token_manager.add_token(str_res, str_res)
            return str_res
        except Exception:
            return "Error"