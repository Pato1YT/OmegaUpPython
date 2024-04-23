def cubomagico(matriz):
    n = len(matriz)
    sumatoria = n*(n**2+1)//2
    
    for i in range(n):
        if sum(matriz[i])!=sumatoria:
            return False
        
        if sum(matriz[j][i] for j in range(n))!=sumatoria:
            return False

    if sum(matriz[i][i] for i in range(n))!=sumatoria:
            return False
    
    if sum(matriz[i][n-i-1] for i in range(n))!=sumatoria:
            return False
    
    return True
        
def matrizcuadrada(n):

    matriz = []

    for i in range(n):
        fila = []
        for j in range(n):
            j = int(input())
            fila.append(j)
    
        matriz.append(fila)
        
    return matriz

n = int(input())
m = int(input())

matrizfinal = matrizcuadrada(n)

if cubomagico(matrizfinal):
    print("True")
else:
    print("False")