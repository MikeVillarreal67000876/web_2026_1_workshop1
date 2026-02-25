import math
from collections import Counter

class Stats:

    def promedio(self, datos):
        if not datos:
            return 0
        return sum(datos) / len(datos)

    def mediana(self, datos):
        if not datos:
            return 0
        datos_ordenados = sorted(datos)
        n = len(datos_ordenados)
        mitad = n // 2

        if n % 2 == 1:
            return float(datos_ordenados[mitad])
        else:
            return (datos_ordenados[mitad - 1] + datos_ordenados[mitad]) / 2

    def moda(self, datos):
        if not datos:
            return None
        contador = Counter(datos)
        return contador.most_common(1)[0][0]

    def varianza(self, datos):
        if not datos:
            return 0
        prom = self.promedio(datos)
        return sum((x - prom) ** 2 for x in datos) / len(datos)

    def desviacion_estandar(self, datos):
        return math.sqrt(self.varianza(datos))

    def rango(self, datos):
        if not datos:
            return 0
        return max(datos) - min(datos)