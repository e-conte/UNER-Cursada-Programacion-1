#   PARTE 2 - ESTRUCTURAS DE CONTROL
#   Que el usuario ingrese dos números y muestre cuál de los dos es menor. Considerar el caso
#   en que ambos números son iguales.

def comparacion_de_numeros():

    def ingresa_numero (texto_adicional):
        return input("Ingresa un número " + texto_adicional)
    #   encapsulamos para utilizar varias veces

    def validamos_numero (texto_adicional):
        es_numero=False
        while es_numero == False:
        #   mientras no sea numero repetimos el loop
            try:
                numero = float (ingresa_numero(texto_adicional))
                es_numero = True
            except:
                continue
            #   Try nos permite hacer un "if" existe error, entonces ejecuta la excepecion
        return numero
    
    def comparacion():
        numero_1= validamos_numero("para comparar si es mayor o menor: ")
        numero_2= validamos_numero("más para comprar si es mayor o menor: ")
        
        def texto_resultado(texto_adicional):
            print(str (numero_1) + " es " + texto_adicional + " que " + str (numero_2))
        
        if numero_1 > numero_2:
            texto_resultado("mayor")
        elif numero_1 < numero_2:
            texto_resultado("menor")
        else:
            texto_resultado("igual")       
    
    return comparacion()

comparacion_de_numeros()