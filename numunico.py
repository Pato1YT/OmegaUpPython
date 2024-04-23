n = int(input())

list = []

for i in range(n):
    i = int(input())
    list.append(i)
    
for elem in list:
    contador = list.count(elem)
    if contador == 1:
        print(elem)