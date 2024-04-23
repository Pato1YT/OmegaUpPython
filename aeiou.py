import re

def contar_vocales(cadena):
    vocales = re.findall(r"[aeiouAEIOU]", cadena)
    cantidad_vocales = len(vocales)
    return cantidad_vocales

n = str(input())

print(len(n))

resultado = contar_vocales(n)
print(resultado)

print(n[::-1])