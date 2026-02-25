class Magic:

    def fibonacci(self, n: int):
        if n < 0:
            return None
        if n == 0:
            return 0
        if n == 1:
            return 1

        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    def secuencia_fibonacci(self, n: int):
        if n < 0:
            return None
        if n == 0:
            return []

        secuencia = []
        for i in range(n):
            secuencia.append(self.fibonacci(i))
        return secuencia

    def es_primo(self, n: int):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def generar_primos(self, n: int):
        if n < 2:
            return []
        return [i for i in range(2, n + 1) if self.es_primo(i)]

    def es_numero_perfecto(self, n: int):
        if n <= 0:
            return False
        suma = 0
        for i in range(1, n):
            if n % i == 0:
                suma += i
        return suma == n

    def triangulo_pascal(self, n: int):
        if n <= 0:
            return None

        triangulo = []
        for i in range(n):
            fila = [1] * (i + 1)
            for j in range(1, i):
                fila[j] = triangulo[i - 1][j - 1] + triangulo[i - 1][j]
            triangulo.append(fila)
        return triangulo

    def factorial(self, n: int):
        if n < 0:
            return None
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

    def mcd(self, a: int, b: int):
        while b != 0:
            a, b = b, a % b
        return abs(a)

    def mcm(self, a: int, b: int):
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // self.mcd(a, b)

    def suma_digitos(self, n: int):
        return sum(int(d) for d in str(abs(n)))

    def es_numero_armstrong(self, n: int):
        if n < 0:
            return False
        digitos = [int(d) for d in str(n)]
        potencia = len(digitos)
        return sum(d ** potencia for d in digitos) == n

    def es_cuadrado_magico(self, matriz):
        if not matriz or not all(len(fila) == len(matriz) for fila in matriz):
            return False

        n = len(matriz)
        suma_magica = sum(matriz[0])

        # Filas
        for fila in matriz:
            if sum(fila) != suma_magica:
                return False

        # Columnas
        for col in range(n):
            if sum(matriz[fila][col] for fila in range(n)) != suma_magica:
                return False

        # Diagonales
        if sum(matriz[i][i] for i in range(n)) != suma_magica:
            return False
        if sum(matriz[i][n - 1 - i] for i in range(n)) != suma_magica:
            return False

        return True