def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1) 

nombres = input()

nom_sep = nombres.split()

cant_nom = len(nom_sep)

if "Ricardo" in nombres:
    cant_nom-=1
    
if "Mirón" in nombres:
    cant_nom-=1
    
    
#print(cant_nom)

n = factorial(cant_nom)
#print(n)

cuatro = factorial(4)
#print(cuatro)

restante = factorial(cant_nom-4)
#print(restante)

resultado = n//(cuatro*restante)

print (resultado)