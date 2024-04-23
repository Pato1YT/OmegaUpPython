numeros = input()

numeros = list(map(int, numeros.split()))

numeros = list(set(numeros))

numeros.sort(reverse=True)

print(numeros)