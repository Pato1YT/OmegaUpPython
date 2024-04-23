def porcentaje(numero, porcentaje):
    resultado = numero * (porcentaje/100)
    return resultado

def descuento(n):
    
    if n < 500:
        return n
    elif n >= 500 and n<=1000:
        valor = porcentaje(n, 5)
        valor = n - valor
        return valor
    elif n>=1001 and n<=7000:
        valor = porcentaje(n, 11)
        valor = n - valor
        return valor
    elif n>=7001 and n<=15000:
        valor = porcentaje(n, 18)
        valor = n - valor
        return valor
    elif n>15000:
        valor = porcentaje(n, 25)
        valor = n - valor
        return valor


cadena = str(input())

valores = cadena.split()
for i in valores:
  i = float(i)
    
  res = descuento(i)
  res = "{:.2f}".format(res)
  print(res)