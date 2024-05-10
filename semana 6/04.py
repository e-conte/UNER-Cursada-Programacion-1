#   PARTE 1 - FUNCIONES
#   4. Que dada la base y altura de un triángulo nos calcule su área.

def area_triangulo ():
    
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
    
    return print(validacion_es_numero_y_es_positivo("la base del triángulo: ") * validacion_es_numero_y_es_positivo("la altura del triangulo: ")/2)
    #   calculamos...

area_triangulo()
