def paréntesis_cerrados(s):
    pila = []
    for char in s:
        if char == '(':
            pila.append(char)
        elif char == ')':
            if not pila or pila[-1] != '(':
                return False
            pila.pop()
    return len(pila) == 0

cadena = input()
if paréntesis_cerrados(cadena):
    print("SI")
else:
    print("NO")
