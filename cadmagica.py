def esMagica(cadena):
    longitud = len(cadena)
    
    if longitud % 2 == 0 and 10>= longitud <=20:
        return True
    else:
        return False
    

cadena = str(input())


if(esMagica(cadena)):
    print("true")
else:
    print("false")