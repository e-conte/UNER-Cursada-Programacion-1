#   7. Escriba un programa Python que cuente con dos listas, la primera de ellas almacenará strings
#   con tareas pendientes y la segunda almacenará strings con tareas terminadas. Permita al
#   usuario:
#   a. Agregar nuevas tareas pendientes.
#   b. Marcar las tareas pendientes como terminadas. Al hacer esto, la tarea deberá pasar
#   de la lista de pendientes a la de terminadas.
#   Nota: posterior a cada operación deberá mostrar por pantalla el estado actual de ambas
#   listas.

def ejercicio_7 ():
    tareas_pendientes = []
    tareas_realizadas = []

    def espacio():
         print("*****************************************************")
    #   Utilizaremos espacios para que sea menos confusa la visualización
    def presentar_tareas (tipo, tarea):
        espacio()
        espacio()
        contador = 0
        print ("Tareas " + tipo + ":")
        for elemento in tarea:
            print("* "+ str(contador) + " *** " + str(elemento) + " * ")
            contador +=1
        #   Agregamos indice + tarea

    def estado_tareas():
        presentar_tareas("pendientes.", tareas_pendientes)
        presentar_tareas("realizadas.", tareas_realizadas)
    #   Agregamos ambas tareas para presentar

    def agregar_tareas ():
        tarea_nueva = input ( "Ingrese una tarea nueva para agregar: ")
        tareas_pendientes.append(tarea_nueva)
    #   agregamos una nueva tarea al final de la lista
        estado_tareas()
    #   mostramos estado
        menu()
    #   volvemos al menu

    def marcar_tareas_pendientes():
        tarea = input ("ingrese el número de tarea a marcar para finalizar: ")
        if tarea.isdigit == False:
            marcar_tareas_pendientes()
        #   validamos que sea un entero positivo
        elif int(tarea) < len(tareas_pendientes):
        #   si esta dentro del rango movemos la tarea, sino con el else volvemos a preguntar
                    tarea=int(tarea)
                    tareas_realizadas.append(tareas_pendientes[tarea])
                    tareas_pendientes.pop(tarea)
                    estado_tareas()
        else:
             marcar_tareas_pendientes()    
        menu()
    #   volvemos al menu luego de finalizar la tarea

    def menu ():
        espacio()
        eleccion = input ("Presiona 1 para Agregar una tarea, o 2 para pasar una tarea a Completada, o enter para salir. ")
        match eleccion:
            case "1":
                agregar_tareas()
            case "2":
                marcar_tareas_pendientes()
            case "":
                exit()   
            case default:
                print("Valor incorrecto")
                menu()
            #   en caso de no haber ingresado las opciones anteriores volvemos al menu y marcamos el error
    menu ()

ejercicio_7 ()