from collections import Counter

n = int(input("Ingrese la cantidad de elementos: "))

lista = []

contador = Counter()  # Usando Counter para contar eficientemente los elementos

for i in range(n):
    valor = int(input(f"Ingrese el valor {i + 1}: "))
    lista.append(valor)
    contador[valor] += 1  # Actualizar el contador mientras llenamos la lista

lista.sort()

for elemento, cantidad in lista and contador:
    print(f"{elemento}: {cantidad}")
