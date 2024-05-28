#   5. Escriba un programa Python que solicite al usuario el ingreso de números enteros. Cuando el
#   usuario ingrese la palabra “fin” el programa deberá concluir con la carga de datos.  Cada uno
#   de los números ingresados por el usuario deberá ser almacenado en una lista. A
#   continuación, realice las siguientes tareas:
#   a. Determinar el máximo.
#   b. Obtener segundo valor máximo. Es decir el que le sigue al máximo.
#   c. Determinar el mínimo.
#   d. Calcular la multiplicación de  todos los números de la lista.
#   e. Contar los valores pares e impares.
#   f. Remover los elementos repetidos

def ejercicio_5():
    lista = []
    def espacio():
        print("********************************************************")
    
    def ingresa_numeros():
        contador = False

        while contador != "fin" :
            nuevo_ingreso = input("Ingresa un número para añadir a la lista, fin para terminar: ")
            if nuevo_ingreso.lower() == "fin":
            #   validamos el ingreso en minúscula de fin
                break
            else:
                try:
                    nuevo_ingreso = int(nuevo_ingreso)
                    lista.append(nuevo_ingreso)
                #   Agregamos el entero negativo o positivo, por eso no comparamos con isdigit que solo valida positivos
                except ValueError:
                    ingresa_numeros()     

    def punto_a():
        espacio()
        print("Punto A")
        lista.sort()
        #   ordenamos la lista
        print("El número más alto es el número: " + str(lista[len(lista)-1]))

    def punto_b():
        print("Punto B")
        print("El número anterior al máximo es el número: " + str(lista[len(lista)-2]))
        #   aprovechamos que ya tenemos la lista ordenada del ejercicio anterior

    def punto_c():
        print("Punto C")
        print("El valor mínimo es el número: " + str(lista[0]))
        #   Igual, como la lista esta ordenada, buscamos el valor mínimo

    def punto_d(): 
        print("Punto D")
        resultado=1
        for numero in lista:
            if numero != 0 :
                resultado*=numero
            else :
                resultado = 0
                break
        print("El resultado de la multiplicación de todos los elementos es: " + str(resultado))

    def punto_e():
        print("Punto E")
        par = impar = 0

        for numero in lista :
            if numero != 0:
                if numero%2 == 0:
                    par+=1
                else:
                    impar+=1
        
        print("La lista tiene " + str(par) + " números pares y " + str(impar) + " números impares.")
        
    def punto_f():
        print("Punto F")
        lista_nueva = []
        for elementos in lista:
        #   para todos los elementos de la lista
            if elementos not in lista_nueva:
            #   si no estan en la lista nueva se agregan
                lista_nueva.append(elementos)
        print("Lista sin valores repetidos")
        print(lista_nueva)


    ingresa_numeros()
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

ejercicio_5()