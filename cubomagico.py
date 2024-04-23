def es_cubo_magico(matriz):
    n = len(matriz)
    target_sum = n * (n**2 + 1) // 2

    for i in range(n):
        if sum(matriz[i]) != target_sum:
            return False
        if sum(matriz[j][i] for j in range(n)) != target_sum:
            return False

    if sum(matriz[i][i] for i in range(n)) != target_sum:
        return False
    if sum(matriz[i][n - i - 1] for i in range(n)) != target_sum:
        return False

    return True

def obtener_matriz_cuadrada(n):
    matriz = []

    for i in range(n):
        fila = []
        for j in range(n):
            valor = int(input())
            fila.append(valor)
        matriz.append(fila)
    return matriz

tamano = int(input())
t = int(input())

matriz_usuario = obtener_matriz_cuadrada(tamano)

if es_cubo_magico(matriz_usuario):
    print("True")
else:
    print("False")
