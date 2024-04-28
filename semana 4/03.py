# 3. Solicite al usuario su nombre y luego solicite su apellido y por último muestre el mensaje de
# salida “Hola nombre apellido”.

def nombre_apellido ():
    nombre = input ("Hola!, por favor escribe tu nombre.")
    apellido = input ("Ahora, por favor escribe tu apellido.")
    return print ("Hola " + nombre + " " + apellido)

nombre_apellido()