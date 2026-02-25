class Magic:

    # ── Fibonacci ──────────────────────────────────────────────

    def fibonacci(self, n: int) -> int:
        if n < 0:
            raise ValueError("n debe ser >= 0")
        if n == 0:
            return 0
        if n == 1:
            return 0

        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    def secuencia_fibonacci(self, n: int) -> list:
        if n <= 0:
            return []
        return [self.fibonacci(i) for i in range(n)]

    # ── Primos ─────────────────────────────────────────────────

    def es_primo(self, n: int) -> bool:
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def generar_primos(self, n: int) -> list:
        return [i for i in range(2, n + 1) if self.es_primo(i)]

    # ── Números especiales ─────────────────────────────────────

    def es_numero_perfecto(self, n: int) -> bool:
        if n <= 1:
            return False
        suma = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                suma += i
                if i != n // i:
                    suma += n // i
        return suma == n

    def es_numero_armstrong(self, n: int) -> bool:
        if n < 0:
            return False
        digitos = [int(d) for d in str(n)]
        potencia = len(digitos)
        return sum(d ** potencia for d in digitos) == n

    # ── Pascal ─────────────────────────────────────────────────

    def triangulo_pascal(self, filas: int) -> list:
        if filas <= 0:
            return []
        triangulo = []
        for i in range(filas):
            fila = [1] * (i + 1)
            for j in range(1, i):
                fila[j] = triangulo[i - 1][j - 1] + triangulo[i - 1][j]
            triangulo.append(fila)
        return triangulo

    # ── Factorial ──────────────────────────────────────────────

    def factorial(self, n: int) -> int:
        if n < 0:
            raise ValueError("n debe ser >= 0")
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

    # ── MCD / MCM ──────────────────────────────────────────────

    def mcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return abs(a)

    def mcm(self, a: int, b: int) -> int:
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // self.mcd(a, b)

    # ── Dígitos ────────────────────────────────────────────────

    def suma_digitos(self, n: int) -> int:
        return sum(int(d) for d in str(abs(n)))

    # ── Cuadrado mágico ────────────────────────────────────────

    def es_cuadrado_magico(self, matriz: list) -> bool:
        if not matriz or any(len(fila) != len(matriz) for fila in matriz):
            return False

        n = len(matriz)
        suma_objetivo = sum(matriz[0])

        for fila in matriz:
            if sum(fila) != suma_objetivo:
                return False

        for col in range(n):
            if sum(matriz[fila][col] for fila in range(n)) != suma_objetivo:
                return False

        if sum(matriz[i][i] for i in range(n)) != suma_objetivo:
            return False

        if sum(matriz[i][n - i - 1] for i in range(n)) != suma_objetivo:
            return False

        return True