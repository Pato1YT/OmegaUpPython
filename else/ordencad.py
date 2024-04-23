import re

def orden_alfabetico(cadena):
    # Eliminar espacios y signos ortográficos de la cadena
    cadena_sin_espacios = re.sub(r'\s+', '', cadena)
    cadena_sin_signos = re.sub(r'[^\w\s]', '', cadena_sin_espacios)

    # Ordenar la cadena sin modificar los espacios y signos ortográficos
    cadena_ordenada = ''.join(sorted(cadena_sin_signos))

    # Reconstruir la cadena con los espacios y signos ortográficos
    resultado = ''
    indice = 0
    for caracter in cadena:
        if caracter.isalpha():
            resultado += cadena_ordenada[indice]
            indice += 1
        else:
            resultado += caracter
    return resultado

# Ejemplo de uso
cadena = input()
cadena_ordenada = orden_alfabetico(cadena)
print(cadena_ordenada)
