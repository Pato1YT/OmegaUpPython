pal = input()
n = input()

n_sep = n.split()

contador = int(0)

for elem in n_sep:
    if elem == pal:
        contador+=1

print(pal, "se repite", contador, "veces.")