n = int(input())

lista = []

for i in range(3):
    elem = str(input())
    lista.append(elem)

for elemento in lista:
    cadmax = elemento.upper()
    cadmin = elemento.lower()
    print(cadmax)
    print(cadmin)