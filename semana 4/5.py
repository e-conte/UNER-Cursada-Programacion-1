# ATENCIÓN: Por una cuestión de legibilidad dejaremos un espacio al final cuando pidamos 
# que el usuario ingrese algún dato.

# 5. Escriba un programa que pida al usuario que ingrese 3 números. Sume los dos primeros y
# luego multiplique este total por el tercero. Mostrar la respuesta en pantalla de la siguiente
# forma: “La respuesta es XX”

import re
#Utilizamos la librería para usar expresiones regulares. 

flotantesPositivos = r'^-?[0-9]*\.?[0-9]+$'
# Detectaremos solo los números flotantes excluyendo letras y caracteres especiales con esta expresión.
numeroParaSumar = otroNumeroParaSumar = numeroParaMultiplicarLaSuma= ""

# Comparamos el contenido de los números con la expresión regular utilizando re.match()
while True :
        if re.match (flotantesPositivos, numeroParaSumar) :
           break
        else :
           numeroParaSumar = input ("Ingresa un número para realizar la suma. ")
           #Mientras no se ingresen números repetiremos la petición al usuario.

while True :
        if re.match (flotantesPositivos, otroNumeroParaSumar) :
           break
        else :
           otroNumeroParaSumar = input ("Ingresa otro número para realizar la suma. ")
           #Mientras no se ingresen números repetiremos la petición al usuario.

while True :
        if re.match (flotantesPositivos, numeroParaMultiplicarLaSuma) :
           break
        else :
           numeroParaMultiplicarLaSuma = input ("Ingresa otro número para multiplicar la suma. ")
        #Mientras no se ingresen números repetiremos la petición al usuario.

print ("La respuesta es " + str (( float (numeroParaSumar) + float (otroNumeroParaSumar)) * float (numeroParaMultiplicarLaSuma)))