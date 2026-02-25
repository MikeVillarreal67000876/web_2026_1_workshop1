import math


class Geometria:

    # ---------------------
    # FIGURAS PLANAS
    # ---------------------

    def area_rectangulo(self, base, altura):
        if base < 0 or altura < 0:
            return 0
        return base * altura

    def perimetro_rectangulo(self, base, altura):
        if base < 0 or altura < 0:
            return 0
        return 2 * (base + altura)

    def area_circulo(self, radio):
        if radio < 0:
            return 0
        return math.pi * radio ** 2

    def perimetro_circulo(self, radio):
        if radio < 0:
            return 0
        return 2 * math.pi * radio

    def area_triangulo(self, base, altura):
        if base < 0 or altura < 0:
            return 0
        return (base * altura) / 2

    def perimetro_triangulo(self, a, b, c):
        if a < 0 or b < 0 or c < 0:
            return 0
        return a + b + c

    def es_triangulo_valido(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            return False
        return a + b > c and a + c > b and b + c > a

    def area_trapecio(self, base_mayor, base_menor, altura):
        if base_mayor < 0 or base_menor < 0 or altura < 0:
            return 0
        return ((base_mayor + base_menor) * altura) / 2

    def area_rombo(self, diagonal_mayor, diagonal_menor):
        if diagonal_mayor < 0 or diagonal_menor < 0:
            return 0
        return (diagonal_mayor * diagonal_menor) / 2

    # ---------------------
    # POLÍGONOS REGULARES
    # ---------------------

    def perimetro_poligono_regular(self, n, lado):
        if n < 0 or lado < 0:
            return 0
        return n * lado

    def area_poligono_regular(self, n, lado, apotema):
        if n < 0 or lado < 0 or apotema < 0:
            return 0
        perimetro = n * lado
        return (perimetro * apotema) / 2

    def perimetro_pentagono_regular(self, lado):
        if lado < 0:
            return 0
        return 5 * lado

    def area_pentagono_regular(self, lado, apotema):
        if lado < 0 or apotema < 0:
            return 0
        return (5 * lado * apotema) / 2

    def perimetro_hexagono_regular(self, lado):
        if lado < 0:
            return 0
        return 6 * lado

    def area_hexagono_regular(self, lado, apotema):
        if lado < 0 or apotema < 0:
            return 0
        return (6 * lado * apotema) / 2

    # ---------------------
    # SÓLIDOS
    # ---------------------

    def volumen_cubo(self, lado):
        if lado < 0:
            return 0
        return lado ** 3

    def area_superficie_cubo(self, lado):
        if lado < 0:
            return 0
        return 6 * lado ** 2

    def volumen_esfera(self, radio):
        if radio < 0:
            return 0
        return (4 / 3) * math.pi * radio ** 3

    def area_superficie_esfera(self, radio):
        if radio < 0:
            return 0
        return 4 * math.pi * radio ** 2

    def volumen_cilindro(self, radio, altura):
        if radio < 0 or altura < 0:
            return 0
        return math.pi * radio ** 2 * altura

    def area_superficie_cilindro(self, radio, altura):
        if radio < 0 or altura < 0:
            return 0
        return 2 * math.pi * radio * (radio + altura)

    # ---------------------
    # GEOMETRÍA ANALÍTICA
    # ---------------------

    def punto_medio(self, x1, y1, x2, y2):
        return ((x1 + x2) / 2, (y1 + y2) / 2)