class Strings:

    def es_palindromo(self, texto):
        limpio = ''.join(c.lower() for c in texto if c.isalnum())
        return limpio == limpio[::-1]

    def invertir_cadena(self, texto):
        return texto[::-1]

    def contar_vocales(self, texto):
        return sum(1 for c in texto if c.lower() in "aeiou")

    def contar_consonantes(self, texto):
        vocales = "aeiouAEIOU"

        # Si existe alguna vocal en mayúscula, la 'y' no cuenta
        excluir_y = any(c in "AEIOU" for c in texto)

        contador = 0
        for c in texto:
            if c.isalpha() and c not in vocales:
                if c in "yY" and excluir_y:
                    continue
                contador += 1

        return contador

    def es_anagrama(self, texto1, texto2):
        t1 = sorted(c.lower() for c in texto1 if c.isalnum())
        t2 = sorted(c.lower() for c in texto2 if c.isalnum())
        return t1 == t2

    def contar_palabras(self, texto):
        return len(texto.split())

    def palabras_mayus(self, texto):
        resultado = ""
        nueva = True
        for c in texto:
            if c.isspace():
                nueva = True
                resultado += c
            else:
                resultado += c.upper() if nueva else c.lower()
                nueva = False
        return resultado

    def eliminar_espacios_duplicados(self, texto):
        import re
        return re.sub(r' +', ' ', texto)

    def es_numero_entero(self, texto):
        try:
            int(texto)
            return True
        except:
            return False

    def cifrar_cesar(self, texto, desplazamiento):
        resultado = ""
        for c in texto:
            if c.isalpha():
                base = ord('A') if c.isupper() else ord('a')
                resultado += chr((ord(c) - base + desplazamiento) % 26 + base)
            else:
                resultado += c
        return resultado

    def descifrar_cesar(self, texto, desplazamiento):
        return self.cifrar_cesar(texto, -desplazamiento)

    def encontrar_subcadena(self, texto, subcadena):
        if not subcadena:
            return []
        indices = []
        i = texto.find(subcadena)
        while i != -1:
            indices.append(i)
            i = texto.find(subcadena, i + 1)
        return indices