#   PARTE 2 - ESTRUCTURAS DE CONTROL
#   6.  Que pida al usuario una palabra y la muestre por pantalla 10 veces.

def string_10_veces():
    palabra = ""
    while palabra == "":
        palabra = input("Ingresa una palabra para verla en pantalla 10 veces: ")
    #   Validamos el ingreso
    return print(palabra*10)
    # imprimimos

string_10_veces()
