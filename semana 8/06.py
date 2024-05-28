#   6. Programe una aplicación de consola Python que brinde al usuario la posibilidad de a partir
#   de una lista vacía:
#   a. Agregar un elemento al final.
#   b. Agregar un elemento al principio.
#   c. Quitar un elemento al final.
#   d. Quitar un elemento al principio.

def ejercicio_6 ():
    lista = []

    def espacio():
        print ("*******************************************")
    #   Adicionamos un separador

    def ingrese_numero(texto_adicional):
        return input ("Ingrese un número " + texto_adicional)
    #   Adicionamos una f() común

    def aviso_final():
        print ("La lista se modificado " + str(lista))
        espacio()
        sigue_o_finaliza()
    #   Con esta f() informamos la modificación y generamos la opción de continuar o no

    def opcion_a ():
        lista.append(ingrese_numero ("para agregarlo al final de la lista: "))
        aviso_final()
    #   realizamos el cambio solicitado

    def opcion_b ():
        lista.insert(0,ingrese_numero ("para agregarlo al principio de la lista: "))
        aviso_final()
    #   realizamos el cambio solicitado

    def opcion_c ():
        lista.pop()
        aviso_final()
    #   realizamos el cambio solicitado

    def opcion_d():
        lista.remove(lista[0])
        aviso_final()
    #   realizamos el cambio solicitado

    def sigue_o_finaliza ():
        print("¿Quiere seguir modificando la lista?")
        eleccion = input ("Presione Enter para Seguir u otra tecla para Salir")
        espacio()
        if eleccion != "":
            quit()
        else:
            ingrese_una_opcion()
    #   De esta manera no tenemos que validar ningún carácter en especial, solo espacio vació o salir.

    def ingrese_una_opcion():
        validador = False
        global opcion
        #   opcion va a ser usada en las f()a/b/c/d por eso la asignamos como global
        espacio()
        print ("Elija una opción:")
        print ("a - Para agregar un elemento al final")
        print ("b - Para agregar un elemento al principio")
        print ("c - Quitar un elemento del final")
        print ("d - Quitar un elemento del principio")
        print ("Lista actual: " + str(lista))
        espacio()
        opcion =input ("Opción:" )
        espacio()
        while validador == False:
            #   validamos la opción y la derivamos a donde corresponde y rompemos el bucle
            match opcion:
                case "a":
                    opcion_a()
                    validador=True
                    break
                case "b":
                    opcion_b()
                    validador=True
                    break
                case "c":
                    opcion_c()
                    validador=True
                    break
                case "d":
                    opcion_d()
                    validador=True
                    break
                case _:
                    print("No elegiste una opción correcta, elije nuevamente")
                    ingrese_una_opcion()

    ingrese_una_opcion()


ejercicio_6()