n = int(input())
num = input().split()

arr = []

for numero in num:
    arr.append(int(numero))

#for i in range(n):
#    num = int(input())
#    arr.append(num)
    
maximo = max(arr)
minimo = min(arr)

print(minimo," ",maximo)
    