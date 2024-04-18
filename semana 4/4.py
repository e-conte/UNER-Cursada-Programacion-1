# ATENCIÓN: Por una cuestión de legibilidad dejaremos un espacio al final cuando pidamos 
# que el usuario ingrese algún dato.

# 4. Pida al usuario que ingrese 2 números para luego sumarlos y mostrar en pantalla: “La
# respuesta es XX”.

import re
#Utilizamos la librería para usar expresiones regulares. 

flotantesPositivos = r'^-?[0-9]*\.?[0-9]+$'
# Detectaremos solo los números flotantes excluyendo letras y caracteres especiales con esta expresión.
numeroParaSumar = otroNumeroParaSumar= ""

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

print ("La respuesta es " + str ( float(numeroParaSumar) + float (otroNumeroParaSumar)))
