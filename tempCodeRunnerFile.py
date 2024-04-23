import math

# Solicitar al usuario que ingrese los coeficientes a, b y c
a = int(input())
b = int(input())
c = int(input())

# Calcular el discriminante (parte dentro de la raíz cuadrada)
discriminante = b**2 - 4*a*c

# Verificar el valor del discriminante para determinar las soluciones
if discriminante > 0:
    # Dos soluciones reales diferentes
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)
    print(x1, x2)
elif discriminante == 0:
    # Una solución real única (raíz doble)
    x1 = -b / (2*a)
    print(x1)
else:
    # No hay soluciones reales (soluciones complejas)
    parte_real = -b / (2*a)
    parte_imaginaria = math.sqrt(abs(discriminante)) / (2*a)
    #print("No hay soluciones reales. Las soluciones complejas son:")
    print(parte_real, "+", parte_imaginaria)
    print(parte_real, "-", parte_imaginaria)