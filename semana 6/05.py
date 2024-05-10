#   PARTE 1 - FUNCIONES
#   5. Que dado tres números ingresados por el usuario nos devuelva el promedio.

def promedio_de_3_numeros():
    
        def ingresa_numero (texto_adicional):
            return input("Ingresa " + texto_adicional)
    #   encapsulamos para utilizar varias veces

        def validacion_es_numero_y_es_positivo (texto_adicional):
            es_positivo=False
            while es_positivo == False:
            #   mientras no sea positivo repetimos el loop
                try:
                    numero = float (ingresa_numero(texto_adicional))
                    if numero >= 0:
                        es_positivo = True
                except:
                    continue
                #   Try nos permite hacer un "if" existe error, entonces ejecuta la excepecion
            return numero
        
        return print((validacion_es_numero_y_es_positivo("un número positivo: ")+ validacion_es_numero_y_es_positivo("otro número: ")+ validacion_es_numero_y_es_positivo("un ultimo número para calcular el promedio: "))/3)

promedio_de_3_numeros()