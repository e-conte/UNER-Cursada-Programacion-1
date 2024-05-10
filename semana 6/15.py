#   PARTE 2 - ESTRUCTURAS DE CONTROL
#   Que solicite al usuario una letra y, si es una vocal, muestre el mensaje “es vocal”. Se debe
#   validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter,
#   informarle que no se puede procesar el dato.

def es_vocal():

    def ingresa_letra():
        caracter=""
        caracter=input("Ingresa un caracter: ")
        if caracter.isalpha() == False or len(caracter) >1:
        # comparamos longitud y que sea caracter
            print("ERROR, no se puede procesar el dato, intente nuevamente.")
            exit()
        else:
            return caracter
    
    def calculo(letra):
        for i in "aeiou":
        #   comparamos vocales y salimos ni bien detecta un "si"
            if letra == i :   
                print("Es vocal.")
                letra=True
                break
        if letra != True:
            print("No es vocal.")
                

    calculo(ingresa_letra())

es_vocal()

