import math


class Geometria:

    # ===============================
    # BÁSICOS
    # ===============================
    def area_rectangulo(self, base, altura):
        if base < 0 or altura < 0:
            return 0
        return base * altura

    def area_circulo(self, radio):
        if radio < 0:
            return 0
        return math.pi * radio ** 2

    def area_triangulo(self, base, altura):
        if base < 0 or altura < 0:
            return 0
        return (base * altura) / 2

    def es_triangulo_valido(self, a, b, c):
        return a + b > c and a + c > b and b + c > a

    # ===============================
    # TRAPECIO / ROMBO
    # ===============================
    def area_trapecio(self, base_mayor, base_menor, altura):
        if base_mayor < 0 or base_menor < 0 or altura < 0:
            return 0
        return ((base_mayor + base_menor) * altura) / 2

    def area_rombo(self, d1, d2):
        if d1 < 0 or d2 < 0:
            return 0
        return (d1 * d2) / 2

    # ===============================
    # PENTÁGONO
    # ===============================
    def area_pentagono_regular(self, perimetro, apotema):
        if perimetro < 0 or apotema < 0:
            return 0
        return (perimetro * apotema) / 2

    def perimetro_pentagono_regular(self, lado):
        if lado < 0:
            return 0
        return 5 * lado

    # ===============================
    # HEXÁGONO
    # ===============================
    def area_hexagono_regular(self, perimetro, apotema):
        if perimetro < 0 or apotema < 0:
            return 0
        return (perimetro * apotema) / 2

    def perimetro_hexagono_regular(self, lado):
        if lado < 0:
            return 0
        return 6 * lado

    # ===============================
    # CUBO
    # ===============================
    def volumen_cubo(self, lado):
        if lado < 0:
            return 0
        return lado ** 3

    def area_superficie_cubo(self, lado):
        if lado < 0:
            return 0
        return 6 * lado ** 2

    # ===============================
    # ESFERA
    # ===============================
    def area_superficie_esfera(self, radio):
        if radio < 0:
            return 0
        return 4 * math.pi * radio ** 2

    # ===============================
    # CILINDRO
    # ===============================
    def volumen_cilindro(self, radio, altura):
        if radio < 0 or altura < 0:
            return 0
        return math.pi * radio ** 2 * altura

    def area_superficie_cilindro(self, radio, altura):
        if radio < 0 or altura < 0:
            return 0
        return 2 * math.pi * radio * (radio + altura)

    # ===============================
    # GEOMETRÍA ANALÍTICA
    # ===============================
    def distancia_entre_puntos(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def punto_medio(self, x1, y1, x2, y2):
        return ((x1 + x2) / 2, (y1 + y2) / 2)

    def pendiente_recta(self, x1, y1, x2, y2):
        if x2 - x1 == 0:
            return None
        return (y2 - y1) / (x2 - x1)

    def ecuacion_recta(self, x1, y1, x2, y2):
        A = y2 - y1
        B = x1 - x2
        C = x2 * y1 - x1 * y2
        return (A, B, C)

    # ===============================
    # POLÍGONO REGULAR GENERAL
    # ===============================
    def area_poligono_regular(self, lados, longitud_lado, apotema):
        if lados < 3 or longitud_lado < 0 or apotema < 0:
            return 0
        perimetro = lados * longitud_lado
        return (perimetro * apotema) / 2

    def perimetro_poligono_regular(self, lados, longitud_lado):
        if lados < 3 or longitud_lado < 0:
            return 0
        return lados * longitud_lado