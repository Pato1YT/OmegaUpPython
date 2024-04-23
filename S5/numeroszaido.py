""""
import math

def esPrimo(numero):
    if numero < 2:
        return False
    # Comprobamos si el número es divisible por algún número menor que él mismo
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def tieneRaiz(numero):
    raiz = math.sqrt(numero)
    esPrimo(raiz)
    
    if esPrimo:
        return True
    return False

numero = int(input())
numero_auxiliar = numero

list = []
listC = []

for i in range(numero):
    if numero_auxiliar % numero == 0:
        esPrimo(numero_auxiliar)
        tieneRaiz(numero_auxiliar)
        if esPrimo:
            list.append(numero_auxiliar)
            print("Si es primo")
        if tieneRaiz:
            listC.append(numero_auxiliar)
            print("Si es primo con raiz")
        numero_auxiliar-=1
    
sum = int(0)    

for elem in list:
    sum+=elem
    
for elem2 in listC:
    sum+=pow(elem2, 2)

print(sum)
"""

import math

def esPrimo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def esDivisor(numero_i):
    raiz = pow(numero_i, 2)
    if numero % int(raiz) == 0:
            return raiz
    else:
        if numero % numero_i == 0:
            return numero_i

numero = int(input())
numero_auxiliar = numero

lista = []
lista_con_raiz = []

for i in range(int(numero)):
    if numero % numero_auxiliar == 0:
        if esPrimo(numero_auxiliar):
            lista.append(esDivisor(numero_auxiliar))
    numero_auxiliar -= 1
    
suma = int(0)

for elem in lista:
    suma += elem
    
#print(suma)    
division = numero/suma
#print(division)

if division.is_integer():
    print("A wilson Zaido")
else:
    print("Chaaale")