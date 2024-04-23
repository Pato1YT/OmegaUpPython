import string

def contiene_abecedario(cadena):
    letras_en_cadena = set(cadena)
    letras_abecedario = set(string.ascii_lowercase)
    return letras_abecedario.issubset(letras_en_cadena)

n = int(input())

mi_lista = []

for i in range(n):
    texto = str(input())
    resultado = contiene_abecedario(texto)
    if resultado:
        print("PERFECT")
    else:
        print("NO WAY")
