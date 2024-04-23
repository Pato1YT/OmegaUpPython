import math as mt

n = float(input())

raiz = mt.sqrt(n)

if raiz.is_integer:
    print("si",int(raiz))
else:
    print("no")