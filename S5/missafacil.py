def potencia(numero, exp):
    resultado = pow(numero, exp)
    return resultado

datos = input()

n, p = datos.split()

n = str(n)
p = int(p)
#n = str(input())

#p = int(input())

sumador = int(0)

for i in n:
    res = potencia(int(i), p)
    sumador+=res
    
if sumador == int(n):
    print ("Simón Missa")
else:
    print ("Nelpas Mijo")