import random


class Games:

    # =====================================================
    # PIEDRA PAPEL TIJERA
    # =====================================================
    def piedra_papel_tijera(self, jugador1, jugador2):
        jugador1 = jugador1.lower()
        jugador2 = jugador2.lower()

        opciones = {"piedra", "papel", "tijera"}

        if jugador1 not in opciones or jugador2 not in opciones:
            return "invalid"

        if jugador1 == jugador2:
            return "empate"

        reglas = {
            "piedra": "tijera",
            "tijera": "papel",
            "papel": "piedra"
        }

        if reglas[jugador1] == jugador2:
            return "jugador1"
        else:
            return "jugador2"

    # =====================================================
    # ADIVINAR NÚMERO
    # =====================================================
    def adivinar_numero_pista(self, numero_secreto, intento):
        if intento == numero_secreto:
            return "correcto"
        elif intento > numero_secreto:
            return "muy alto"
        else:
            return "muy bajo"

    # =====================================================
    # TA TE TI (solo filas y columnas)
    # =====================================================
    def ta_te_ti_ganador(self, tablero):

        # Filas
        for fila in tablero:
            if fila[0] == fila[1] == fila[2] and fila[0] != " ":
                return fila[0]

        # Columnas
        for col in range(3):
            if tablero[0][col] == tablero[1][col] == tablero[2][col] and tablero[0][col] != " ":
                return tablero[0][col]

        # Si hay espacios → continúa
        for fila in tablero:
            if " " in fila:
                return "continua"

        # Si está lleno y nadie ganó → empate
        return "empate"

    # =====================================================
    # MASTERMIND
    # =====================================================
    def generar_combinacion_mastermind(self, longitud, colores):
        return [random.choice(colores) for _ in range(longitud)]

    # =====================================================
    # AJEDREZ - TORRE
    # =====================================================
    def validar_movimiento_torre_ajedrez(self,
                                         fila_origen, col_origen,
                                         fila_destino, col_destino,
                                         tablero):

        if not (0 <= fila_origen < 8 and 0 <= col_origen < 8 and
                0 <= fila_destino < 8 and 0 <= col_destino < 8):
            return False

        if fila_origen == fila_destino and col_origen == col_destino:
            return False

        if fila_origen != fila_destino and col_origen != col_destino:
            return False

        if fila_origen == fila_destino:
            paso = 1 if col_destino > col_origen else -1
            for c in range(col_origen + paso, col_destino, paso):
                if tablero[fila_origen][c] != " ":
                    return False

        if col_origen == col_destino:
            paso = 1 if fila_destino > fila_origen else -1
            for f in range(fila_origen + paso, fila_destino, paso):
                if tablero[f][col_origen] != " ":
                    return False

        return True