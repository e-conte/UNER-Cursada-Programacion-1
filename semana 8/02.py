#   2. Pedir al usuario que ingrese 5 números para luego almacenarlos en una lista y ordenarlos.
#   Imprimir por pantalla el resultado.

def ejercicio_2 ():
    lista = []    
    def ingresa_numero ():
        return input ("Por favor ingresa un número: ")

    def crea_lista ():
        contador = 0
        numero_ingresado = ""

        while contador != 5:
            contador+=1
            numero_ingresado = ingresa_numero()
            lista.append(numero_ingresado)
            #   Agregamos el nuevo numero a la lista predefinida
        return lista

    crea_lista()
    print (lista)
    
ejercicio_2()
        

