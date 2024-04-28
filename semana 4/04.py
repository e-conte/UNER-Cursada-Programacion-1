# 4. Pida al usuario que ingrese 2 números para luego sumarlos y mostrar en pantalla: “La
# respuesta es XX”.

def suma():
    numero_para_sumar = input ("Ingresa un número para realizar la suma.")
    otro_numero_para_sumar = input ("Ingresa otro número para realizar la suma.")
    return print ("La respuesta es " + str ( float(numero_para_sumar) + float (otro_numero_para_sumar)))

suma()