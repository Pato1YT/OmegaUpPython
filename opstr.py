cadena = input()

palabras = cadena.split()

for i, palabra in enumerate(palabras):
    if i % 2 == 0:
        palabras[i] = palabra.lower()
    else:
        palabras[i] = palabra.upper()
        
cadenam = " ".join(palabras)

print(cadenam)