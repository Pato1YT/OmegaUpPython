import re

def contarVocales(cadena):

    cantVocales = re.findall('[aeiouAEIOU]', cadena)
    return len(cantVocales)

def contarConsonates(cadena):
    


cadena = str(input())

cadenas = cadena.split()

n_palabras = len(cadenas)

