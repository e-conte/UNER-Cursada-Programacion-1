#   Dada la siguiente lista de frutas [“banana”, “manzana”, “pera”], permitir al usuario ingresar 3
#   frutas más para agregarlas al final de lista. Luego, mostrar por pantalla la lista completa y
#   debajo la misma lista pero sólo con las frutas que añadió el usuario.

def ejercicio_3 ():
    lista = ["banana", "manzana", "pera"]
    lista_nueva = []

    def ingresar_fruta ():
        return input ("Ingresa una fruta: ")

    def añadir_fruta ():
        contador = 0

        while contador != 3:
            contador += 1
            fruta_nueva = ingresar_fruta()
            lista_nueva.append(fruta_nueva)
            #   Agregamos las 3 nuevas frutas a la lista nueva
            lista.append(fruta_nueva)
            #   Agregamos las 3 nuevas frutas a la lista inicial
        return lista_nueva

    def imprime_en_pantalla ():
        print (lista)
        print (lista_nueva)

    añadir_fruta()
    imprime_en_pantalla()


ejercicio_3()