import math

class ScientificFunctions:
    def __init__(self):
        self.angle_mode = "Rad"  # Peut être "Rad" ou "Deg"

    def set_angle_mode(self, mode):
        if mode in ["Rad", "Deg"]:
            self.angle_mode = mode

    def _to_rad(self, val):
        if self.angle_mode == "Deg":
            return math.radians(val)
        return val

    def _from_rad(self, val):
        if self.angle_mode == "Deg":
            return math.degrees(val)
        return val

    # Trigonométrie standard
    def sin(self, x):
        return math.sin(self._to_rad(x))

    def cos(self, x):
        return math.cos(self._to_rad(x))

    def tan(self, x):
        return math.tan(self._to_rad(x))

    # Fonctions réciproques (Trigonométrie)
    def asin(self, x):
        return self._from_rad(math.asin(x))

    def acos(self, x):
        return self._from_rad(math.acos(x))

    def atan(self, x):
        return self._from_rad(math.atan(x))

    # Fonctions hyperboliques
    def sinh(self, x):
        return math.sinh(x)

    def cosh(self, x):
        return math.cosh(x)

    def tanh(self, x):
        return math.tanh(x)

    # Fonctions hyperboliques réciproques
    def asinh(self, x):
        return math.asinh(x)

    def acosh(self, x):
        return math.acosh(x)

    def atanh(self, x):
        return math.atanh(x)

    # Fonctions de puissance et racines complexes
    def cube_root(self, x):
        if x < 0:
            return -(-x) ** (1/3)
        return x ** (1/3)

    def log_y(self, x, y):
        return math.log(x, y)

    def factorial(self, x):
        if x < 0:
            raise ValueError("Math Error")
        return math.factorial(int(x))