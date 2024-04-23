n = int(input())

lista = []
contador=0

for i in range(n):
    elem=str(input())
    lista.append(elem)
    
for o in lista:
    for t in o:
        if(t == " "):
            contador+1
print(contador)
            


