#   PARTE 2 - ESTRUCTURAS DE CONTROL
#   Que imprima el siguiente patrón:
#
#   5 4 3 2 1
#   4 3 2 1
#   3 2 1
#   2 1 
#   1
#
def imprime_patron():

    def impresion_vertical():
        contador=5
        while contador > 0:
            impresion_horizontal(contador)
            contador-=1
        #   utilizamos el contador para iterar horizontalmente en la función que sigue
    def impresion_horizontal(x):
        jota = ""
        while x > 0:
            jota=jota + " " + str(x)
            x-=1
        print (jota)
        # sumamos en cada loop un string horizontal, en total 5 veces es llamada esta f() por la f()vertical

    impresion_vertical()
imprime_patron()
