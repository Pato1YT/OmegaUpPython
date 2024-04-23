def es_casilla_negra(fila, columna):
    """
    Determina si una casilla dada en un tablero de ajedrez es negra o blanca.

    Parámetros:
        fila (int): Número de fila (1-8).
        columna (str): Letra de columna (a-h).

    Retorna:
        bool: True si la casilla es negra, False si es blanca.
    """
    columnas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    indice_columna = columnas.index(columna.lower())

    # Si la suma de los índices de fila y columna es par, la casilla es blanca.
    if (fila + indice_columna) % 2 == 0:
        return False
    else:
        return True

# Pedir la posición al usuario
posicion = input()
columna, fila = posicion.split()
#columna = input()
#fila = int(input())
fila = int(fila)

# Verificar si la casilla es negra o blanca
casilla_negra = es_casilla_negra(fila, columna)

# Imprimir el resultado
if casilla_negra:
    print("NEGRO")
else:
    print("BLANCO")
