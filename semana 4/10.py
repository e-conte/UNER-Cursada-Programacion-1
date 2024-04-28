#   10. Escriba un programa que indique si un texto es palíndromo, es decir, se escribe igual al
#   derecho que al revés. Por ejemplo: rayar, kayak, somos.


def palíndromo():
        texto_ingresado = input ("Ingresa un texto para verificar si es un palíndromo.")
        texto_ingresado = texto_ingresado.upper()
        texto_ingresado_al_reves = texto_ingresado [::-1]
        if texto_ingresado == texto_ingresado_al_reves:
                print("es palíndromo")
        else:
                print("no es palíndromo")
palíndromo()