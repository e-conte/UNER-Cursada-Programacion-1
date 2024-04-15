# ATENCIÓN: Por una cuestión de legibilidad dejaremos un espacio al final cuando pidamos 
#           que el usuario ingrese algún dato.

# 1. Mostrar por pantalla: “Hola Mundo, esto es Python!”.

print ("Hola Mundo, Esto es Python!")



# 2. Escriba un programa que solicite el nombre del usuario y luego muestre el mensaje de salida
# “Hola nombre”, donde nombre es el nombre que ingresó el usuario.

nombre = input ("Hola!, por favor escribe tu nombre. ")

print ("Hola " + nombre)



# 3. Solicite al usuario su nombre y luego solicite su apellido y por último muestre el mensaje de
# salida “Hola nombre apellido”.

nombre = input ("Hola!, por favor escribe tu nombre. ")
apellido = input ("Ahora, por favor escribe tu apellido. ")

print ("Hola " + nombre + " " + apellido)



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



#   9. Pida al usuario que ingrese un texto para luego imprimirlo al revés. Ej: HOLA -> ALOH.

textoIngresado = input ("Ingresa un texto que luego será impreso al revés. ")

print ( textoIngresado [::-1])



#   10. Escriba un programa que indique si un texto es palíndromo, es decir, se escribe igual al
#   derecho que al revés. Por ejemplo: rayar, kayak, somos.

textoIngresado = input ("Ingresa un texto para verificar si es un palíndromo. ")

textoIngresado = textoIngresado.upper()
#Pasamos a mayúsculas todo el texto, para poder realizar posteriormente la comparación. 

textoIngresadoAlReves = textoIngresado [::-1]
#Colocamos el texto al reverso en una nueva variable

if  textoIngresado == textoIngresadoAlReves :
        print ("El texto es un palíndromo.")
else :
        print ("El texto no es un palíndromo.")

#   11 Programe una aplicación de consola que muestre los primeros 5 caracteres de una cadena
#   de texto ingresada por el usuario.

textoIngresado = ""

while len (textoIngresado) < 5 :
        textoIngresado = input("Ingrese un texto de al menos 5 caracteres, luego será cortado y mostraremos los primeros 5 caracteres. ")        
#repetiremos la petición al usuario hasta que ingrese un texto con 5 o más caracteres

print (textoIngresado [0:5])

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
           int (fechaIngresada)
           break
        else:
           fechaIngresada = input("Ingresa una fecha con el formato dd/mm/aaaa. ")
           #Mientras no se ingresen números enteros positivos repetiremos la petición al usuario.

print ("Día: ", fechaIngresada [0:2],", Mes: ", fechaIngresada [2:4]," y Año: ", fechaIngresada [4:8])

#   13. Programe una aplicación de consola que solicite al usuario su nombre, después su apellido y
#   a continuación su año de nacimiento. Con esos datos deberá generar una sugerencia de
#   usuario y contraseña. Por ejemplo: nombre: Martín, apellido: Francisconi, Año nacimiento:
#   1985 -> Usuario: mfrancisconi, Contraseña: mf.1985.

nombre = input ("Hola!, por favor escribe tu nombre. ")
apellido = input ("Ahora, por favor escribe tu apellido. ")
añoDeNacimiento = input ("Finalmente, por favor escribe el año en que naciste. ")

#Mediremos el largo de los datos, los cortaremos de forma aleatoria y los uniremos creando usuario y contraseña.

nombreLength = len(nombre)
apellidoLength = len (apellido)
añoDeNacimientoLength = len (añoDeNacimiento)

import random 
# importamos la librería random con la cual obtendremos números random.

numeroDeCorteDelNombre = random.randint (1,nombreLength)

numeroDeCorteDelApellido = random.randint (1,apellidoLength)
#numeroRandom definido desde uno hasta el número máximo de letras del apellido.

numeroDeCorteDelAñoDeNacimiento = random.randint (1,añoDeNacimientoLength) 
#numeroRandom definido desde uno hasta el número máximo de letras del año de nacimiento.

usuario = nombre [0:1] + "." + apellido  
#separamos una letra del nombre, sumamos "." y apellido

contraseña = nombre [0:numeroDeCorteDelNombre] + "#" + apellido [0:numeroDeCorteDelApellido] + "#" + añoDeNacimiento [0:numeroDeCorteDelAñoDeNacimiento] 
#sumamos un corte en cada dato, adicionamos # y concatenamos

print ("El usuario Sugerido es: " + usuario + " La contraseña sugerida es: " + contraseña)