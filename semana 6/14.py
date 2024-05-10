#   PARTE 2 - ESTRUCTURAS DE CONTROL
#   Que pida un año y que escriba si es bisiesto o no. Les recordamos que los años bisiestos son
#   múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí. Algunos
#   ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900
#   no es bisiesto.

def bisiesto():

    def ingresa_numero():
        numero=input("Ingresa un número de año paras saber si es biciesto: ")
        if numero.isdigit() != True:
            biciesto()
        else:
            return int (numero)
    
    def calculo(numero):
        if (numero % 4 == 0  and numero % 100 != 0) or (numero % 100 == 0 and numero % 400 == 0):
            print("El año es bisiesto.")
        else:
            print("El año no es bisiesto.")
    
    calculo(ingresa_numero())

bisiesto()