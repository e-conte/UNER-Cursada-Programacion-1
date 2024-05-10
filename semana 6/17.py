#   PARTE 2 - ESTRUCTURAS DE CONTROL
#   17. Que muestre todos los números primos entre 0 y 100 e imprima cuántos números primos hay.

def numeros_primos():
    numero_auxiliar=""    
    def ingresa_numero(numero):
        numero=input("Ingresa un número para validar si es o no primo: ")
        if numero == "":
            ingresa_numero(numero_auxiliar)
        elif numero.isdigit() == True:
            numero = int (numero)
            return numero
        else:
            ingresa_numero(numero_auxiliar)
        #   Validamos != "" u cualquier otra entrada != de entero positivo
        
    
    def calculo(numero):
        contador= numero-1
        resultado=False
        while contador >= 2:
        #   empezamos desde el 2, xq dividir por 1 haría que todos sean primos
            if (numero % contador) == 0:
                resultado = True
                break
            else:
                contador-=1
        if resultado == False:
            print("Es un número primo")
        else:
            print("No es un número primo")            

    calculo(ingresa_numero(numero_auxiliar))

numeros_primos()    