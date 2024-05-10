#   PARTE 2 - ESTRUCTURAS DE CONTROL
#   Pedir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro
#   mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día
#   ingresado no es ninguno de esos, imprimir otro mensaje.

def dias_de_la_semana():
    dia=input("Ingrese un día de la semana: ").lower()

    match dia:
        case "lunes":
            print("Lunes, agua y ajo, empieza la semana.")
        case "martes":
            print("Martes, ideal para ir al gimnasio.")
        case "miércoles":
            print("A mitad de todo o mitad de nada!.")
        case "jueves":
            print("Sale peña con amigos.")
        case "viernes":
            print("Al fin viernes!!")
        case "sábado":
            print("Hermoso día para salir a disfrutar con amigos.")
        case "domingo":
            print("A descansar que arrancamos de nuevo.")       
        case default:
            dias_de_la_semana()
        #   en caso de no haber ingresado un día de la semana volvemos al inicio


dias_de_la_semana()
