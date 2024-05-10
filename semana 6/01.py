#   PARTE 1 - FUNCIONES
#   Que al pasarle una cadena <nombre> nos muestre por pantalla el saludo ¡Hola <nombre>!.
    
def saludo ( nombre = "" ):

    def ingresa_nombre () :
        return input( "Ingresa tu nombre: " )
    #creamos una función auxiliar  
    
    while nombre == "":
    #   mientras no se ingrese nombre, repetiremos la función auxiliar ingresa_nombre
        nombre = ingresa_nombre ()

    return print ( "¡Hola " + nombre + "!" )

saludo()