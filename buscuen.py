n = int(input())

list = []

for i in range(n):
    i = int(input())
    list.append(i)
    
bus = int(input())
cont = int(0)

for elem in list:
    if elem == bus:
        cont+=1

print(cont)