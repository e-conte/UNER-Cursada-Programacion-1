#   8. Escriba un programa que permita al usuario ingresar la base y altura de un triángulo para
#   luego imprimir por pantalla la superficie total.

def superficie_triangulo():
    base_del_triangulo = input ("Ingresa el valor de la base del triangulo." )
    altura_del_triangulo = input ("Ingresa el valor de la altura del triangulo.")
    return print(( float (base_del_triangulo) * float (altura_del_triangulo)) / 2)

superficie_triangulo()