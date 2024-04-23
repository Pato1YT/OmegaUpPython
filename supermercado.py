datos = input()

n, m = datos.split()

n = int(n)
m = int(m)
sum = int(0)

list = []

for i in range(n):
    i = int(input())
    list.append(i)
    
for elem in list:
    if elem <= m and sum!=m:
        print("pasa")
        sum+=elem
    else:
        print("espera")
    
    
