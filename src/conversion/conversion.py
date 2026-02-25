class Conversion:

    # 🌡️ Temperatura
    def celsius_a_fahrenheit(self, celsius: float) -> float:
        return celsius * 9 / 5 + 32

    def fahrenheit_a_celsius(self, fahrenheit: float) -> float:
        return (fahrenheit - 32) * 5 / 9

    # 📏 Longitud
    def metros_a_pies(self, metros: float) -> float:
        return metros * 3.28084

    def pies_a_metros(self, pies: float) -> float:
        return pies / 3.28084

    # 🔢 Binario / Decimal
    def decimal_a_binario(self, numero: int) -> str:
        if numero < 0:
            return None
        return bin(numero)[2:]

    def binario_a_decimal(self, binario: str) -> int:
        try:
            return int(binario, 2)
        except ValueError:
            return None

    # 🏛️ Romano / Decimal
    def decimal_a_romano(self, numero: int) -> str:
        if numero <= 0:
            return None

        valores = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
            (1, "I")
        ]

        resultado = ""
        for valor, simbolo in valores:
            while numero >= valor:
                resultado += simbolo
                numero -= valor

        return resultado

    def romano_a_decimal(self, romano: str) -> int:
        valores = {
            "I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100,
            "D": 500, "M": 1000
        }

        total = 0
        prev = 0

        for letra in reversed(romano):
            valor = valores.get(letra)
            if valor is None:
                return None
            if valor < prev:
                total -= valor
            else:
                total += valor
                prev = valor

        return total

    # 📡 Morse
    def texto_a_morse(self, texto: str) -> str:
        morse = {
            "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
            "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
            "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
            "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
            "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
            "Z": "--.."
        }

        resultado = []
        for letra in texto.upper():
            if letra == " ":
                resultado.append("/")
            elif letra in morse:
                resultado.append(morse[letra])
            else:
                return None

        return " ".join(resultado)

    def morse_a_texto(self, codigo: str) -> str:
        morse = {
            ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
            "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
            "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
            ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
            "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
            "--..": "Z"
        }

        resultado = []
        for simbolo in codigo.split():
            if simbolo == "/":
                resultado.append(" ")
            elif simbolo in morse:
                resultado.append(morse[simbolo])
            else:
                return None

        return "".join(resultado)