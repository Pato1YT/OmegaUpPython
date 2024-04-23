calificaciones = input()

num1, num2, num3, num4, num5, num6, num7 = calificaciones.split()

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
num4 = int(num4)
num5 = int(num5)
num6 = int(num6)
num7 = int(num7)

promedio = (num1+num2+num3+num4+num5+num6+num7)/7

promedio = float(promedio)
resultado = format(promedio, ".1f")

print(resultado)

