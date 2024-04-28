# 5. Escriba un programa que pida al usuario que ingrese 3 números. Sume los dos primeros y
# luego multiplique este total por el tercero. Mostrar la respuesta en pantalla de la siguiente
# forma: “La respuesta es XX”

def resultado():
    numero_para_sumar = input ("Ingresa un número para realizar la suma.")
    otro_numero_para_sumar = input ("Ingresa otro número para realizar la suma.")
    numero_para_multiplicar_la_suma = input ("Ingresa otro número para multiplicar la suma.")
    return print ("La respuesta es " + str (( float (numero_para_sumar) + float (otro_numero_para_sumar)) * float (numero_para_multiplicar_la_suma)))

resultado()