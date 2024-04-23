cadlet = input()
cadena, letra = cadlet.split()

contador = int(0)

for caracter in cadena:
    if caracter == letra:
        contador+=1
        
print(contador)