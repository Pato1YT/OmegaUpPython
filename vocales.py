cadena = str(input())

list = {"a", "i", "u", "e", "o"}
contador = int(0)

for caracter in cadena:
    if caracter in list:
        contador+=1

print(contador)