#   PARTE 1 - FUNCIONES
#   2. Que reciba un número entero positivo y una potencia a elevar y que nos devuelva el resultado.

def potencia_de_un_numero ():
    variable_auxiliar = False
    #   ambas variables las inicializamos para que activen el loop del while

    def ingresa_numero (texto_adicional):
        return input("Ingresa un número " + texto_adicional)
    #   Utilizaremos una f() auxiliar

    def validacion_entero_positivo():
        entero_positivo=""
        while entero_positivo.isdigit() == False:
                 entero_positivo = ingresa_numero("entero positivo. ")
        #   validamos que sea entero positivo
        return entero_positivo

    def validacion_potencia():
        potencia=""
        while variable_auxiliar == False:
            try:
            #   la f() try intenta ejecutar el código si no puede, ejecuta la excepción
                potencia= int(potencia)
                break
            #   validamos si la potencia es entera positiva o negativa 
            except ValueError:
                potencia= ingresa_numero("que será potencia del anterior. ")
        return potencia

    def calculo_potencia():
        print(int(validacion_entero_positivo())**validacion_potencia())
    #   imprimimos la cuenta
    calculo_potencia()

potencia_de_un_numero()