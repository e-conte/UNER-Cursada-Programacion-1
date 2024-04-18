# ATENCIÓN: Por una cuestión de legibilidad dejaremos un espacio al final cuando pidamos 
# que el usuario ingrese algún dato.

#   12. Pedir al usuario que ingrese una fecha en formato dd/mm/aaaa e imprimir en pantalla el
#   día, mes y año. Ej:
#   Usuario ingresa: 17/05/1985
#   Programa imprime: Día: 17, Mes: 05 y Año: 1985

import re
#Utilizamos la librería para usar expresiones regulares. 

enterosSinElCero = r'^[1-9][0-9]*$'
# Detectaremos solo los números enteros positivos excluyendo letras y caracteres especiales con esta expresión.
fechaIngresada ="" 

while True:
        if (re.match(enterosSinElCero, fechaIngresada[0:2]) and re.match(enterosSinElCero, fechaIngresada[2:4]) and re.match(enterosSinElCero, fechaIngresada[4:8])):
           break
        else:
           fechaIngresada = input("Ingresa una fecha con el formato dd/mm/aaaa. ")
           #Mientras no se ingresen números enteros positivos repetiremos la petición al usuario.

print ("Día: ", fechaIngresada [0:2],", Mes: ", fechaIngresada [2:4]," y Año: ", fechaIngresada [4:8])