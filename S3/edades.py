n = int(input())

valores = input()

valores_sep = valores.split()

list = [int(valor) for valor in valores_sep]

list.sort()
    
contador = {}

for elemento in list:
    if elemento in contador:
        contador[elemento]+=1
    else:
        contador[elemento] = 1
        
for elemento, cantidad in contador.items():
    print(elemento, cantidad)