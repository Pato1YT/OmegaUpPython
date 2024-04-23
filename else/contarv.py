def contar_numero(arreglo, nb):
    contador = 0
    for numero in arreglo:
        if numero == nb:
            contador+= 1
    
    return contador


n = int(input())
nb = int(input())



arreglo = []

for i in range(n):
        numero = int(input())
        arreglo.append(numero)

repeticiones = contar_numero(arreglo, nb)
print(repeticiones)