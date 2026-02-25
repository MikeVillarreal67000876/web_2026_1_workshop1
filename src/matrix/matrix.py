class Matrix:

    def matriz_transpuesta(self, matriz):
        # Caso matriz vacía
        if not matriz:
            return []

        filas = len(matriz)
        columnas = len(matriz[0])

        transpuesta = []

        for j in range(columnas):
            nueva_fila = []
            for i in range(filas):
                nueva_fila.append(matriz[i][j])
            transpuesta.append(nueva_fila)

        return transpuesta