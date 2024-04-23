def potencia(numero, exp):
    resultado = pow(numero, exp)
    return resultado

n = str(input())
pot = int(0)
while True:
    sumador = int(0)
    pot+=1
    for i in n:
        res = potencia(int(i), pot)
        sumador+=res
        
    if sumador == int(n):
        print(pot)            
        break
            
    if sumador > int(n):
        break    