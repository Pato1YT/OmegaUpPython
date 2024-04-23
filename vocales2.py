cadena = str(input())

list = {'A', 'I', 'U', 'E', 'O', 'a', 'i', 'u', 'e', 'o'}

while len(cadena) < 4:
    cadena = str(input())
    
contador = int(0)

for e in cadena:
    if e in list:
        contador+=1

print(contador)