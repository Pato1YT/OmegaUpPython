r = input()


n1, n2, n3, n4 = r.split()

n1= int(n1)
n2= int(n2)
n3= int(n3)
n4= int(n4)

rango1= range(n1, n2)
rango2= range(n3,n4)

if rango1.stop >= rango2.start and rango1.start <= rango2.stop:
    print("1")
else:
    print("0")

