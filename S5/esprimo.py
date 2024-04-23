def es_primo(numero):
    # Los números menores que 2 no son primos
    if numero < 2:
        return False
    # Comprobamos si el número es divisible por algún número menor que él mismo
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Pedimos al usuario que ingrese un número
num = int(input("Ingrese un número: "))

# Comprobamos si el número es primo o no
if es_primo(num):
    print(num, "es un número primo")
else:
    print(num, "no es un número primo")
