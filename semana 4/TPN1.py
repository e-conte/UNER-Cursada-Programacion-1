# ATENCIÓN: Por una cuestión de legibilidad dejaremos un espacio al final cuando pidamos 
#           que el usuario ingrese algún dato.

# 1. Mostrar por pantalla: “Hola Mundo, esto es Python!”.

print("Hola Mundo, Esto es Python!")

# 2. Escriba un programa que solicite el nombre del usuario y luego muestre el mensaje de salida
# “Hola nombre”, donde nombre es el nombre que ingresó el usuario.

nombre = input("Hola!, por favor escribe tu nombre. ")

print ("Hola " + nombre)

# 3. Solicite al usuario su nombre y luego solicite su apellido y por último muestre el mensaje de
# salida “Hola nombre apellido”.

nombre = input("Hola!, por favor escribe tu nombre. ")
apellido = input("Ahora, por favor escribe tu apellido. ")

print ("Hola " + nombre + " " + apellido)

# 4. Pida al usuario que ingrese 2 números para luego sumarlos y mostrar en pantalla: “La
# respuesta es XX”.

numeroParaSumar = float(input ("Ingresa un número para realizar una suma. "))
otroNumeroParaSumar = float(input ("Ingresa otro número para realizar la suma. "))

print ("La respuesta es " + str(numeroParaSumar + otroNumeroParaSumar))

# 5. Escriba un programa que pida al usuario que ingrese 3 números. Sume los dos primeros y
# luego multiplique este total por el tercero. Mostrar la respuesta en pantalla de la siguiente
# forma: “La respuesta es XX”

numeroParaSumar = float(input ("Ingresa un número para realizar una suma. "))
otroNumeroParaSumar = float(input ("Ingresa otro número para realizar la suma. "))
numeroParaMultiplicarLaSuma = float(input("Ingrese un número adicional para multiplicar la suma de los dos números anteriores. "))

print("La respuesta es " + str((numeroParaSumar+otroNumeroParaSumar)* numeroParaMultiplicarLaSuma))

# 6. Programe una aplicación de consola que pregunte el precio total de la cuenta, luego
# pregunte cuántos comensales hay. A continuación deberá dividir la cuenta total por el
# número de comensales y mostrar cuánto debe pagar cada persona.

precioDeLaCuenta = float(input("¿Cuál es el precio de la cuenta.? "))
cantidadDeComensales = int(input("¿Cuál es la cantidad de comensales.? "))

print("Cada persona debe pagar " + str(precioDeLaCuenta / cantidadDeComensales))

#7. Pida al usuario un número x de días y luego mostrar por pantalla cuántas horas, minutos y
# segundos son esos números de días.

numeroDeDias = int(input("Ingrese el número de días que usted desee. "))
#   Si una hora tiene 3600Segundos, 3600x24hs=86400 Segundos/Día, 60x24=1440Minutos/Día y finalmente 24hs/día

print("El número de días tiene " + str(numeroDeDias*24)+" horas "+ str(numeroDeDias*1440)+" minutos "+ str(numeroDeDias*86400)+ "segundos.")

#   8. Escriba un programa que permita al usuario ingresar la base y altura de un triángulo para
#   luego imprimir por pantalla la superficie total.

baseDelTriangulo = float(input("Ingrese la base del triangulo. "))
alturaDelTriangulo = float(input("Ingrese la altura del triangulo. "))

print("La superficie total del triangulo es: "+ str((baseDelTriangulo*alturaDelTriangulo)/2))

#   9. Pida al usuario que ingrese un texto para luego imprimirlo al revés. Ej: HOLA -> ALOH.

textoIngresado = input("Ingresa un texto que luego será impreso al revés. ")

print( textoIngresado[::-1])

#   10. Escriba un programa que indique si un texto es palíndromo, es decir, se escribe igual al
#   derecho que al revés. Por ejemplo: rayar, kayak, somos.

textoIngresado = input("Ingresa un texto para verificar si es un palíndromo. ")
textoIngresadoAlReves = textoIngresado[::-1]

if  textoIngresado == textoIngresadoAlReves :
        print("El texto es un palíndromo.")
else:
        print("El texto no es un palíndromo.")

#   11 Programe una aplicación de consola que muestre los primeros 5 caracteres de una cadena
#   de texto ingresada por el usuario.

textoIngresado = input("Ingrese un texto de al menos 5 caracteres, luego será cortado y mostraremos los primeros 5 caracteres. ")

print(textoIngresado[0:5])

#   12. Pedir al usuario que ingrese una fecha en formato dd/mm/aaaa e imprimir en pantalla el
#   día, mes y año. Ej:
#   Usuario ingresa: 17/05/1985
#   Programa imprime: Día: 17, Mes: 05 y Año: 1985


fechaIngresada = input("Ingresa una fecha con el formato dd/mm/aaaa. ")

print("Día: ", fechaIngresada[0:2],", Mes: ", fechaIngresada[2:4]," y Año: ", fechaIngresada[4:8])

#   13. Programe una aplicación de consola que solicite al usuario su nombre, después su apellido y
#   a continuación su año de nacimiento. Con esos datos deberá generar una sugerencia de
#   usuario y contraseña. Por ejemplo: nombre: Martín, apellido: Francisconi, Año nacimiento:
#   1985 -> Usuario: mfrancisconi, Contraseña: mf.1985.

nombre = input("Hola!, por favor escribe tu nombre. ")
apellido = input("Ahora, por favor escribe tu apellido. ")
añoDeNacimiento = input("Finalmente, por favor escribe el año en que naciste. ")

#Mediremos el largo de los datos, los cortaremos de forma aleatoria y los uniremos creando usuario y contraseña.

nombreLength = len(nombre)
apellidoLength = len(apellido)
añoDeNacimientoLength = len(añoDeNacimiento)

import random 
# importamos la librería random con la cual obtendremos números random.

numeroDeCorteDelNombre = random.randint(1,nombreLength)

numeroDeCorteDelApellido = random.randint(1,apellidoLength)
#numeroRandom definido desde uno hasta el número máximo de letras del apellido.

numeroDeCorteDelAñoDeNacimiento = random.randint(1,añoDeNacimientoLength) 
#numeroRandom definido desde uno hasta el número máximo de letras del año de nacimiento.

usuario = nombre[0:1]+"."+apellido  
#separamos una letra del nombre, sumamos "." y apellido

contraseña = nombre[0:numeroDeCorteDelNombre]+"#"+apellido[0:numeroDeCorteDelApellido]+"#"+añoDeNacimiento[0:numeroDeCorteDelAñoDeNacimiento] 
#sumamos un corte en cada dato, adicionamos # y concatenamos

print("El usuario Sugerido es: "+ usuario + " La contraseña sugerida es: " + contraseña)