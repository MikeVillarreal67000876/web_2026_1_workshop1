class Logica:

    def AND(self, a: bool, b: bool) -> bool:
        return a and b

    def OR(self, a: bool, b: bool) -> bool:
        return a or b

    def NOT(self, a: bool) -> bool:
        return not a

    def XOR(self, a: bool, b: bool) -> bool:
        return a != b

    def NAND(self, a: bool, b: bool) -> bool:
        return not (a and b)

    def NOR(self, a: bool, b: bool) -> bool:
        return not (a or b)

    def XNOR(self, a: bool, b: bool) -> bool:
        return a == b

    def implicacion(self, a: bool, b: bool) -> bool:
        # a → b es equivalente a ¬a ∨ b
        return (not a) or b

    def bi_implicacion(self, a: bool, b: bool) -> bool:
        # a ↔ b es verdadero cuando ambos son iguales
        return a == 0