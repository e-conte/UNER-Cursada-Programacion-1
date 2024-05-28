#   1. Crear un programa que almacene en una lista las materias de esta u otra carrera y que las
#   muestre por pantalla. (La lista debe ser predefinida, no debe ser ingresada por el usuario).

def ejercicio1():
    lista = ["algrebra", "informatica", "software libre"]
    count = 0

    for element in lista:
        count += 1
        print (str(count) + " - " + element)

ejercicio1()    
