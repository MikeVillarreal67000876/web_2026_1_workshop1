import math


class Geometria:

    # ===============================
    # CUADRADO
    # ===============================
    def area_cuadrado(self, lado):
        return lado * lado

    def perimetro_cuadrado(self, lado):
        return 4 * lado

    # ===============================
    # RECTÁNGULO
    # ===============================
    def area_rectangulo(self, base, altura):
        return base * altura

    def perimetro_rectangulo(self, base, altura):
        return 2 * (base + altura)

    # ===============================
    # TRIÁNGULO
    # ===============================
    def area_triangulo(self, base, altura):
        return (base * altura) / 2

    def perimetro_triangulo(self, lado1, lado2, lado3):
        return lado1 + lado2 + lado3

    # ===============================
    # CÍRCULO
    # ===============================
    def area_circulo(self, radio):
        return math.pi * radio ** 2

    def perimetro_circulo(self, radio):
        return 2 * math.pi * radio

    # ===============================
    # CUBO
    # ===============================
    def volumen_cubo(self, lado):
        return lado ** 3

    # ===============================
    # ESFERA
    # ===============================
    def volumen_esfera(self, radio):
        return (4 / 3) * math.pi * radio ** 3