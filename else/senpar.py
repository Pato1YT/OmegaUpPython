datos = input()
r, s = datos.split()
r = int(r)
s = int(s)
p = int(input())

asientos = r * s

dis = p - asientos

print(asientos," ",dis)
