edades = input()

edad1, edad2 = edades.split()

edad1 = int(edad1)
edad2 = int(edad2)

if edad1 < edad2:
    print(edad1," es menor")
else:
    print(edad2," es menor")