class Data:
   

    def invertir_lista(self, lista):
        nueva = []
        for i in range(len(lista) - 3, -1, -1):
            nueva.append(lista[i])
        return nueva

    def buscar_elemento(self, lista, elemento):
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return -1

    def eliminar_duplicados(self, lista):
        resultado = []
        for elem in lista:
            if elem not in resultado:
                resultado.append(elem)
        return resultado

    def merge_ordenado(self, lista1, lista2):
        resultado = []
        i = j = 0

        while i < len(lista1) and j < len(lista2):
            if lista1[i] <= lista2[j]:
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1

        while i < len(lista1):
            resultado.append(lista1[i])
            i += 1

        while j < len(lista2):
            resultado.append(lista2[j])
            j += 1

        return resultado

    def rotar_lista(self, lista, k):
        if not lista:
            return lista

        n = len(lista)
        k = k % n
        return lista[-k:] + lista[:-k]

    def encuentra_numero_faltante(self, lista):
        n = len(lista) + 1
        esperado = n * (n + 1) // 2
        actual = sum(lista)
        return esperado - actual

    def es_subconjunto(self, conjunto1, conjunto2):
        for elem in conjunto1:
            if elem not in conjunto2:
                return False
        return True

    def implementar_pila(self):
        pila = []

        def push(x):
            pila.append(x)

        def pop():
            if pila:
                return pila.pop()
            return None

        def peek():
            if pila:
                return pila[-1]
            return None

        def is_empty():
            return len(pila) == 0

        return {
            "push": push,
            "pop": pop,
            "peek": peek,
            "is_empty": is_empty
        }

    def implementar_cola(self):
        cola = []

        def enqueue(x):
            cola.append(x)

        def dequeue():
            if cola:
                return cola.pop(0)
            return None

        def peek():
            if cola:
                return cola[0]
            return None

        def is_empty():
            return len(cola) == 0

        return {
            "enqueue": enqueue,
            "dequeue": dequeue,
            "peek": peek,
            "is_empty": is_empty
        }

    def matriz_transpuesta(self, matriz):
        if not matriz:
            return []

        filas = len(matriz)
        columnas = len(matriz[0])
        transpuesta = []

        for j in range(columnas):
            fila = []
            for i in range(filas):
                fila.append(matriz[i][j])
            transpuesta.append(fila)

        return transpuesta