numeros = input()

n1, n2 = numeros.split()
n1= int(n1)
n2= int(n2)


for num in range(n1, n2 + 1):
    if(num % n1 == 0):
        print(num)