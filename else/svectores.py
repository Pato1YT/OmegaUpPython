n = int(input())
num = input().split()
num2 = input().split()

arr = []
arr2 = []

for numero in num:
    arr.append(int(numero))

for numero2 in num2:
    arr2.append(int(numero2))
    
suma = [x + y for x, y in zip(arr, arr2)]
suma = str(suma)

resultado = ' '.join(suma)
print(resultado)