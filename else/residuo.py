def verificar_suma_modulo(num1, num2, n):
    if (num1 + num2) % n == 0:
        return "SI"
    else:
        return "NO"

# Ejemplo de uso:
numero1 = int(input())
numero2 = int(input())
modulo = int(input())
resultado = verificar_suma_modulo(numero1, numero2, modulo)
print(resultado)
