# ATENCIÓN: Por una cuestión de legibilidad dejaremos un espacio al final cuando pidamos 
# que el usuario ingrese algún dato.

#   8. Escriba un programa que permita al usuario ingresar la base y altura de un triángulo para
#   luego imprimir por pantalla la superficie total.

import re
#Utilizamos la librería para usar expresiones regulares. 

flotantesPositivos = r'^(0|[1-9]\d*)(\.\d+)?$'
# Detectaremos solo los números flotantes positivos excluyendo letras y caracteres especiales con esta expresión.
baseDelTriangulo = alturaDelTriangulo = ""
# Comparamos el contenido de los números con la expresión regular utilizando re.match()

while True :
        if re.match (flotantesPositivos, baseDelTriangulo) :
           break
        else :
           baseDelTriangulo = input ("Ingresa el valor de la base del triangulo. " )
           #Mientras no se ingresen números flotantes positivos repetiremos la petición al usuario.

while True:
        if re.match (flotantesPositivos, alturaDelTriangulo) :
           break
        else :
           alturaDelTriangulo = input ("Ingresa el valor de la altura del triangulo. ")
           #Mientras no se ingresen números flotantes positivos repetiremos la petición al usuario.

print("La superficie total del triangulo es: " + str (( float (baseDelTriangulo)* float (alturaDelTriangulo)) / 2))
