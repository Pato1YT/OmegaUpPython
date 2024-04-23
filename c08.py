numeros = input()

n1, n2 = numeros.split()

n1 = int(n1)
n2 = int(n2)

if (n1+n2)%2==0:
    print(int((n1+n2)/2))
else:
    print(float((n1+n2)/2))