#   9. Pida al usuario que ingrese un texto para luego imprimirlo al revés. Ej: HOLA -> ALOH.

def texto_invertido():
    texto_ingresado = input ("Ingresa un texto que luego será impreso al revés.")
    return print ( texto_ingresado [::-1])

texto_invertido()