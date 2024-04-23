n = int(input())

list = []

for i in range(n):
    i = str(input())
    list.append(i)
    
for cadena in list:
    cadtemp = str(cadena[::-1])
    if cadena==cadtemp:
        print("P")
    else:
        print("NP")