anos = input()

ano1, ano2 = anos.split()

ano1 = int(ano1)
ano2 = int(ano2)

edad = ano2-ano1

if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")