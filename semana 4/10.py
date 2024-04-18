# ATENCIÓN: Por una cuestión de legibilidad dejaremos un espacio al final cuando pidamos 
# que el usuario ingrese algún dato.

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