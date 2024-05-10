#   PARTE 2 - ESTRUCTURAS DE CONTROL
#   13. Que resuelva el siguiente problema: los alumnos de un curso se han dividido en dos grupos
#    A y B de acuerdo al sexo y el nombre. El grupo A está formado por las mujeres con un
#   nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el
#   resto. Escribir un programa que pregunte al usuario su nombre y sexo y muestre por pantalla
#   el grupo que le corresponde. 

def seleccion_de_grado():

    def ingresa_nombre():
        nombre = input("Ingrese el nombre del alumno/a.: ").lower()
        if nombre == "" or nombre.isalpha()!= True:
            ingresa_nombre()
        #   validamos letras de la A a la Z
        else:
            global letra
            letra = nombre[:1]
        #   guardamos la 1era letra del nombre
        #   definimos global la variable para reutilizarla luego        

    def ingresa_sexo():
        
            global hombre_o_mujer
            sexo = input("Ingrese si el alumno es hombre o mujer:" ).lower()
            match sexo:
                case "hombre":
                    hombre_o_mujer = sexo
                case "mujer":
                    hombre_o_mujer = sexo
                case default:
                    ingresa_sexo()
                #   en caso de ser distinto a hombre o mujer repetimos el input llamando nuevamente a la f()                
            
    def calculo ():
        letra_a_comparar=letra
        resultado=""
        match hombre_o_mujer:
            case "mujer":
                for i in "abcdefghijkl" :
                    if i == letra_a_comparar:
                        resultado = "Es una alumna mujer del grado A."
                        break
                    else:
                        resultado = "Es una alumna mujer del grado B."
                        break
            case "hombre":
                for i in "opqrstuvwxyz":
                    if i == letra_a_comparar:
                        resultado = "Es un alumno hombre de grado A"
                        break
                    else:
                        resultado = "Es un alumno hombre de grado B"
                        break
        return print(resultado)
    #   recorremos y agregamos break para cortar el loop cuando este el resultado
    #   También podríamos utilizar una función para resultado y acortar la expresión

    ingresa_nombre()
    ingresa_sexo()
    calculo()

seleccion_de_grado()