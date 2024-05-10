#   PARTE 2 - ESTRUCTURAS DE CONTROL
#   Que el usuario ingrese un número entero positivo y muestre por pantalla lo siguiente:
#   a. Todos los números impares desde 1 hasta ese número separados por comas.
#   b. La cuenta atrás desde ese número hasta cero separados por comas.
#   c. Que indique si es primo o no.
#   d. Por último, su factorial.

def ejercicio_10():
    numero_ingresado=""

    def ingresa_numero_positivo():
        numero_positivo = ""
        while numero_positivo.isdigit() == False:
            numero_positivo = input("Ingresa un número positivo: ")
            #validamos que el número sea positivo y entero
        return int (numero_positivo)

    numero_ingresado = ingresa_numero_positivo()
    #   asignamos este numero para utilizarlo en las demás funciones de cada punto
    def numeros_impares_separados_por_comas(numero_positivo):
        numero = numero_positivo
        lista_de_numeros = range(2,numero)
        numero = 1
        #   reasignamos numero para colocarlo primero sin"coma" por eso lista_de_numeros empieza en 2, para darle continuidad
        for contador in lista_de_numeros:
            if contador % 2 != 0:
                numero = str (numero) + "," + str (contador)
                # contamos impares
        return print(numero)

    def cuenta_atras(numero_ingresado):
        numero = contador = numero_ingresado
        lista_numeros = range(1 , (numero + 1))
        #+1 porque "range" excluye el número final  
        for i in lista_numeros:
            contador -=1
            numero = str (numero) + "," + str (contador)
            #   utilizamos contador porque ahora número al agregar "comas" es un string
        return print(numero)
    
    def validador_de_numeros_primos(posible_primo):
        numero = contador = posible_primo
        no_es_primo = True
        for contador in range(2,numero):
            if numero % contador == 0:
                no_es_primo = False
                break
        #   validamos si es o no primo y lo asignamos
        no_es_primo = "El número no es primo." if no_es_primo == False else "El número es primo."
        return print(no_es_primo)

    def factorial(numero_ingresado):
        numero = contador = numero_ingresado
        contador-=1
        for contador in range(2, numero):
        #   similar al caso anterior,empezamos en 2 para evitar una multiplicación x 1 y ahorrar 1 bucle
            numero= numero * contador
            contador-=1
        return print(numero)


    numeros_impares_separados_por_comas(numero_ingresado)
    cuenta_atras(numero_ingresado)
    validador_de_numeros_primos(numero_ingresado)
    factorial(numero_ingresado)

ejercicio_10()