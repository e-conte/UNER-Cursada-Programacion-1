# ATENCIÓN: Por una cuestión de legibilidad dejaremos un espacio al final cuando pidamos 
# que el usuario ingrese algún dato.

#   11 Programe una aplicación de consola que muestre los primeros 5 caracteres de una cadena
#   de texto ingresada por el usuario.

textoIngresado = ""

while len (textoIngresado) < 5 :
        textoIngresado = input("Ingrese un texto de al menos 5 caracteres, luego será cortado y mostraremos los primeros 5 caracteres. ")        
#repetiremos la petición al usuario hasta que ingrese un texto con 5 o más caracteres

print (textoIngresado [0:5])