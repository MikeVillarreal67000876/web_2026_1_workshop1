import random


class Games:

    # =====================================================
    # PIEDRA PAPEL TIJERA
    # =====================================================
    def piedra_papel_tijera(self, jugador1, jugador2):

        opciones = ["piedra", "papel", "tijera"]

        jugador1 = jugador1.lower()
        jugador2 = jugador2.lower()

        if jugador1 not in opciones or jugador2 not in opciones:
            return "invalid"

        if jugador1 == jugador2:
            return "empate"

        if (
            (jugador1 == "piedra" and jugador2 == "tijera") or
            (jugador1 == "papel" and jugador2 == "piedra") or
            (jugador1 == "tijera" and jugador2 == "papel")
        ):
            return "jugador1"

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
    # TA TE TI
    # =====================================================
    def ta_te_ti_ganador(self, tablero):

        # Filas
        for fila in tablero:
            if fila[0] == fila[1] == fila[2] and fila[0] != " ":
                return fila[0]

        # Columnas
        for col in range(3):
            if (
                tablero[0][col] ==
                tablero[1][col] ==
                tablero[2][col] and
                tablero[0][col] != " "
            ):
                return tablero[0][col]

        # Diagonales
        if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != " ":
            return tablero[0][0]

        if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != " ":
            return tablero[0][2]

        # Si hay espacios vacíos → continúa
        for fila in tablero:
            if " " in fila:
                return "continua"

        # Si no hay espacios y no hay ganador → empate
        return "empate"

    # =====================================================
    # MASTERMIND
    # =====================================================
    def generar_combinacion_mastermind(self, longitud, colores):

        return [random.choice(colores) for _ in range(longitud)]

    # =====================================================
    # AJEDREZ - TORRE
    # =====================================================
    def validar_movimiento_torre_ajedrez(
        self,
        fila_origen,
        col_origen,
        fila_destino,
        col_destino,
        tablero
    ):

        # Validar límites del tablero (0-7)
        for valor in [fila_origen, col_origen, fila_destino, col_destino]:
            if valor < 0 or valor > 7:
                return False

        # No puede quedarse en la misma posición
        if fila_origen == fila_destino and col_origen == col_destino:
            return False

        # Debe moverse en línea recta
        if fila_origen != fila_destino and col_origen != col_destino:
            return False

        # Movimiento horizontal
        if fila_origen == fila_destino:
            paso = 1 if col_destino > col_origen else -1
            for c in range(col_origen + paso, col_destino, paso):
                if tablero[fila_origen][c] != " ":
                    return False

        # Movimiento vertical
        if col_origen == col_destino:
            paso = 1 if fila_destino > fila_origen else -1
            for f in range(fila_origen + paso, fila_destino, paso):
                if tablero[f][col_origen] != " ":
                    return False

        return True