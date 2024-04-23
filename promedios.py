calificaciones = input()

cal1, cal2, cal3, cal4, cal5 = calificaciones.split()

cal1 = int(cal1)
cal2 = int(cal2)
cal3 = int(cal3)
cal4 = int(cal4)
cal5 = int(cal5)

promedio = (cal1+cal2+cal3+cal4+cal5)/5 
promedio = int(promedio)
print(promedio)