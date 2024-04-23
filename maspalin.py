n = int(input())
lista = []


for i in range(n):
    elem = str(input())
    lista.append(elem)

for elemento in lista:
    if(elemento[::-1]==elemento):
        print("P")
    else:
        print("NP")
        
