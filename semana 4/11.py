#   11 Programe una aplicación de consola que muestre los primeros 5 caracteres de una cadena
#   de texto ingresada por el usuario.

def primeros_cinco_caracteres():
    texto_ingresado = input("Ingrese un texto de al menos 5 caracteres, luego será cortado y mostraremos los primeros 5 caracteres.")        
    print (texto_ingresado [0:5])

primeros_cinco_caracteres()