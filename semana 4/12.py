#   12. Pedir al usuario que ingrese una fecha en formato dd/mm/aaaa e imprimir en pantalla el
#   día, mes y año. Ej:
#   Usuario ingresa: 17/05/1985
#   Programa imprime: Día: 17, Mes: 05 y Año: 1985

def fecha_formateada():
    fecha_ingresada = input("Ingresa una fecha con el formato dd/mm/aaaa.")
    return print ("Día: " + str(fecha_ingresada [0:2]) + ", Mes: " + str(fecha_ingresada [3:5]) + " y Año: " + str(fecha_ingresada [6:10]))

fecha_formateada()