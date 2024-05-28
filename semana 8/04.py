#   4. Dada la siguiente lista: países = [“Argentina,”Brasil”, “Bolivia”,”Paraguay”,”Venezuela”],
#       realizar lo siguiente:
#   a. Imprimir la cantidad de elementos que tiene la lista.
#   b. Imprimir el primer y último elemento.
#   c. Imprimir el resto.
#   d. Permitir que el usuario ingrese un país e imprimir el índice si el país se encuentra en
#       la lista. Si no se encuentra, imprimir un mensaje advirtiendo al usuario.
#   e. Permitir al usuario ingresar un número igual o menor a la cantidad de elementos de
#       la lista. Quitar el elemento correspondiente de esa posición.
#   f. Imprimir la lista en orden inverso.
#   g. Vaciar la lista.

def ejercicio_4 ():
    def espacio():
        print("--------------------------------------------------------------------------")
    lista = ["Argentina","Brasil", "Bolivia","Paraguay","Venezuela"]

    def punto_a ():
        print("Punto A")
        print (len(lista))

    def punto_b ():
        print("Punto B")
        print (lista[0])
        print (lista[len(lista)-1])

    def punto_c ():
        print ("Punto C")
        print (lista [1:(len(lista)-1)])

    def punto_d ():
        print ("Punto D")
        lista = ["Argentina","Brasil", "Bolivia","Paraguay","Venezuela"]
        #   Agregamos la lista nuevamente porque en el pto anterior la acortamos
        ingrese_pais = (input ( "Ingrese un país nuevo: ")).lower()
        contador = 0
        es_igual= ""
        while contador != (len(lista)) :
            if ingrese_pais != (lista[contador]).lower():
                contador += 1
            else:
                es_igual = contador
                break
        #   Probamos de 0 a el ultimo indice, si nos pasamos entonces no existe.
        if es_igual == len(lista):
            
            print ("El país no se encuentra en la lista")
        else:
            print ("El país de la lista existe y su indice en la lista es: " + str(contador))

    def punto_e() :
        print ("Punto E")
        ingresa_numero=""
        while ingresa_numero == "":
            if ingresa_numero.isdigit() == False:   
                ingresa_numero= input ("Ingresa un número entre 0 y 4: ")
            else:
                break
        #   comprobamos que sea entero positivo
        while int (ingresa_numero) > 5:
                ingresa_numero= input ("Ingresa un número entre 0 y 4: ")
        #   comprobamos que este en el rango de la lista
        lista.pop (int (ingresa_numero))
        #   quitamos el elemento
        print("Se quito el elemento de indice "+ ingresa_numero + " y la lista quedo asi: " + str(lista))

    def punto_f ():
        print("Punto F")
        lista = ["Argentina","Brasil", "Bolivia","Paraguay","Venezuela"]
        #   Agregamos la lista ya que en el punto anterior la modificamos nuevamente.
        lista.reverse()
        print (lista)    

    def punto_g():
        for element in lista:
           lista.remove(element)
        print(lista)
        print("La lista esta vacía.") 

    punto_a()
    espacio()
    punto_b()
    espacio()
    punto_c()
    espacio()
    punto_d()
    espacio()
    punto_e()
    espacio()
    punto_f()
    espacio()
    punto_g()

ejercicio_4()
