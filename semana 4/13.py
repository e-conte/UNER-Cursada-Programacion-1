#   13. Programe una aplicación de consola que solicite al usuario su nombre, después su apellido y
#   a continuación su año de nacimiento. Con esos datos deberá generar una sugerencia de
#   usuario y contraseña. Por ejemplo: nombre: Martín, apellido: Francisconi, Año nacimiento:
#   1985 -> Usuario: mfrancisconi, Contraseña: mf.1985.

def usuario_y_contraseña():
    nombre = input ("Hola!, por favor escribe tu nombre. ").lower()
    apellido = input ("Ahora, por favor escribe tu apellido. ").lower()
    año_de_nacimiento = input ("Finalmente, por favor escribe el año en que naciste. ")
    usuario = nombre [0:1] + apellido  
    contraseña = nombre [0:1] + apellido [0:1] + "." + año_de_nacimiento 
    return print ("Usuario: " + usuario + ", Contraseña: " + contraseña)

usuario_y_contraseña()