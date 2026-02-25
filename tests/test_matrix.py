import pytest
from src.matrix.matrix import Matrix


class TestMatrix:

    def setup_method(self):
        self.matrix = Matrix()

    def test_matriz_transpuesta_2x2(self):
        matriz = [
            [1, 2],
            [3, 4]
        ]
        esperado = [
            [1, 3],
            [2, 4]
        ]
        assert self.matrix.matriz_transpuesta(matriz) == esperado

    def test_matriz_transpuesta_3x2(self):
        matriz = [
            [1, 2],
            [3, 4],
            [5, 6]
        ]
        esperado = [
            [1, 3, 5],
            [2, 4, 6]
        ]
        assert self.matrix.matriz_transpuesta(matriz) == esperado

    def test_matriz_transpuesta_1x3(self):
        matriz = [[1, 2, 3]]
        esperado = [
            [1],
            [2],
            [3]
        ]
        assert self.matrix.matriz_transpuesta(matriz) == esperado

    def test_matriz_transpuesta_cuadrada(self):
        matriz = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        esperado = [
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9]
        ]
        assert self.matrix.matriz_transpuesta(matriz) == esperado

    def test_matriz_transpuesta_con_un_elemento(self):
        matriz = [[42]]
        esperado = [[42]]
        assert self.matrix.matriz_transpuesta(matriz) == esperado

    def test_matriz_transpuesta_vacia(self):
        assert self.matrix.matriz_transpuesta([]) == []