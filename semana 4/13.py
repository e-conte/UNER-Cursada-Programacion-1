# ATENCIÓN: Por una cuestión de legibilidad dejaremos un espacio al final cuando pidamos 
# que el usuario ingrese algún dato.

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