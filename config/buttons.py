BUTTONS_GRID = [
    ["MC", "MR", "M+", "M-", "MS", "M▽"],
    ["2nd", "Rad/Deg", "F-E", "CE", "C", "⌫"],
    ["x²", "cos", "sin", "tan", "(", ")"],
    ["√x", "cosh", "sinh", "tanh", "π", "e"],
    ["xʸ", "|x|", "exp", "mod", "n!", "/"],
    ["10ˣ", "7", "8", "9", "+/-", "*"],
    ["log", "4", "5", "6", "%", "-"],
    ["ln", "1", "2", "3", ",", "+"],
    ["0", ".",  "="]
]

# Changements induits par la touche '2nd' pour la première colonne
SHIFT_FIRST_COL_MAP = {
    "x²": "x³",
    "√x": "∛x",
    "xʸ": "ʸ√x",
    "10ˣ": "2ˣ",
    "log": "logᵧx",
    "ln": "eˣ"
}

# Changements induits par la touche '2nd' pour les fonctions trigonométriques
SHIFT_TRIG_MAP = {
    "sin": "sin⁻¹",
    "cos": "cos⁻¹",
    "tan": "tan⁻¹",
    "sinh": "sinh⁻¹",
    "cosh": "cosh⁻¹",
    "tanh": "tanh⁻¹"
}