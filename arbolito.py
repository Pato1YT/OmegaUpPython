from colorama import Fore, init

init(autoreset=True)

def arbol_navidad_colores(filas):
    for i in range(filas):
        espacios = ' ' * (filas - i - 1)
        asteriscos = '*' * (2 * i + 1)
        if i == 0:
            asteriscos = Fore.YELLOW + '*' + Fore.GREEN + '*' * (2 * i)
        print(Fore.GREEN + espacios + asteriscos)

altura = 10
arbol_navidad_colores(altura)

