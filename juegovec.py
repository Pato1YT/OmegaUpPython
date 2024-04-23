n = int(input())

list = []

for i in range(n):
    i = int(input())
    if i != 0:
        list.append(i)
    else:
        list.clear()
        

if list:
    for i in list:
        print(i)
else:
    print("VACIO")