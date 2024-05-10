#   PARTE 1 - FUNCIONES
# 3. Que nos calcule el total de una factura tras aplicarle el IVA. La función debe recibir la
# cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca
# la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

def precio_con_iva_factura ():
    
    texto_adicional_iva = "correspondiente al valor de IVA que quieres aplicarle a tu factura, presiona enter para asignar 21%. "
    texto_adicional_monto_factura= "que represente el valor de tu factura sin IVA. "
    

    def ingresa_numero (texto_adicional):
        return input("Ingresa un número " + texto_adicional)
    #   encapsulamos para utilizar varias veces

    def validacion_monto_factura (texto_adicional):
        es_positivo=False
        while es_positivo == False:
        #   mientras no sea positivo repetimos el loop
            try:
                numero = float (ingresa_numero(texto_adicional))
                if numero >= 0:
                    es_positivo = True
            except:
                continue
            #   Try nos permite hacer un "if" existe error, entonces ejecuta la excepecion y continua con el while
        return numero


    def validacion_valor_iva (texto_adicional):
        es_positivo = False
        numero="x"
        while es_positivo == False:
            numero = ingresa_numero (texto_adicional_iva)
            if numero == "":
                numero = 21.0
                break
            #   validamos en el 2do loop si el usuario presiono "Enter"
            else:
                try:
                    numero = float (numero)
                    if numero >= 0:
                       es_positivo = True
                    else:
                        continue
                    # si no es numero flotante positivo le pedimos que ingrese nuevamente enviándolo al loop siguiente
                except:
                    continue
            #   aquí lo enviamos al siguiente loop porque no ingreso un número, ya que no se pudo ejecutar el float en número
        return numero
     
    def calculo():
        return print (validacion_monto_factura(texto_adicional_monto_factura) * (1+ validacion_valor_iva (texto_adicional_iva) / 100))               
    #   realizamos el calculo en pantalla                   

    calculo()                     
precio_con_iva_factura ()

#   la forma más fácil que encontre para validad es con expresiones regulares, pero de esta forma practico estructuras
