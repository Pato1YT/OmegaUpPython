def determinar_numero(numero):
    if numero == 0:
        return "Nulo"
    elif numero % 2 == 0:
        return "Par"
    else:
        return "Impar"

# Ejemplo de uso:
numero_ingresado = int(input())
resultado = determinar_numero(numero_ingresado)
print(resultado)
