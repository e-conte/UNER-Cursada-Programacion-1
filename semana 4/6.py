# ATENCIÓN: Por una cuestión de legibilidad dejaremos un espacio al final cuando pidamos 
# que el usuario ingrese algún dato.

# 6. Programe una aplicación de consola que pregunte el precio total de la cuenta, luego
# pregunte cuántos comensales hay. A continuación deberá dividir la cuenta total por el
# número de comensales y mostrar cuánto debe pagar cada persona.

import re
#Utilizamos la librería para usar expresiones regulares. 

flotantesPositivos = r'^\+?\d*\.?\d+$'
# Detectaremos solo los números flotantes positivos excluyendo letras y caracteres especiales para la cuenta.
enterosSinElCero = r'^[1-9][0-9]*$'
# Detectaremos solo los números enteros sin el cero para la cantidad de comensales. 
precioDeLaCuenta = cantidadDeComensales = ""

# Comparamos el contenido de los números con la expresión regular utilizando re.match()
while True :
        if re.match (flotantesPositivos, precioDeLaCuenta) :
           break
        else :
           precioDeLaCuenta = input ("Ingresa el precio de la cuenta. ")
           #Mientras no se ingresen números repetiremos la petición al usuario.

while True :
        if re.match (enterosSinElCero, cantidadDeComensales) :
           break
        else :
           cantidadDeComensales = input ("Ingresa el número de comensales. ")
           #Mientras no se ingresen números distintos a cero repetiremos la petición al usuario.

print ("Cada comensal debe abonar $ " + str ( float (precioDeLaCuenta) / int (cantidadDeComensales)))