#   PARTE 2 - ESTRUCTURAS DE CONTROL
#   8.  Pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

def validador_de_edad():
    edad = ""

    while edad.isdigit() == False:
    #Validamos que sea un entero positivo con isdigit()
        edad = input("Hola, por favor ingresa tu edad, y validaremos si eres mayor: ")

    return print("Eres mayor de edad.") if int (edad) > 17 else print("Eres menor de edad.")

validador_de_edad()
