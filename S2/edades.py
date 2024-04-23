"""
edades = input()

edades = list(map(int, edades.split()))

edades = list(set(edades))

edades.sort(reverse=True)

edades = str(edades)

print(str(edades))
"""

# Solicitar al usuario que ingrese los elementos separados por espacios
entrada_usuario = input()

# Convertir la entrada del usuario a una lista de cadenas
lista_original = entrada_usuario.split()

# Convertir la lista de cadenas a una lista de enteros
lista_enteros = [int(elemento) for elemento in lista_original]

# Ordenar la lista de mayor a menor
lista_ordenada = sorted(lista_enteros, reverse=True)

# Eliminar duplicados manteniendo el orden original
lista_sin_duplicados = sorted(set(lista_ordenada), key=lista_ordenada.index)

# Imprimir la lista en el formato deseado con comillas
print([str(elemento) for elemento in lista_sin_duplicados])


