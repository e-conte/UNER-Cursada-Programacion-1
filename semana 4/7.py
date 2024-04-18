# ATENCIÓN: Por una cuestión de legibilidad dejaremos un espacio al final cuando pidamos 
# que el usuario ingrese algún dato.

#7. Pida al usuario un número x de días y luego mostrar por pantalla cuántas horas, minutos y
# segundos son esos números de días.

import re
#Utilizamos la librería para usar expresiones regulares. 

enteros = r'^(0|[1-9]\d*)$' 
# Detectaremos solo los números enteros positivos excluyendo letras y caracteres especiales con esta expresión.
numeroDeDias = ""

# Comparamos el contenido de los números con la expresión regular utilizando re.match()
while True :
        if re.match (enteros, numeroDeDias) :
           break
        else :
           numeroDeDias = input ("Ingresa otro número de días. ")
           #Mientras no se ingresen números enteros repetiremos la petición al usuario.

print ("El número de días " + numeroDeDias + " tiene " + str ( int(numeroDeDias) * 24)+ " horas " + str ( int (numeroDeDias) * 1440) + " minutos " + str ( int (numeroDeDias) * 86400) + "segundos.")
#   Si una hora tiene 3600Segundos, 3600x24hs=86400 Segundos/Día, 60x24=1440Minutos/Día y finalmente 24hs/día