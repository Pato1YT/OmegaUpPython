n = int(input())

list = []

for i in range(n):
    i = int(input())
    list.append(i)
    
contador = int(0)

for elem in list:
    contador+=elem

resultado = contador/n
print(resultado)