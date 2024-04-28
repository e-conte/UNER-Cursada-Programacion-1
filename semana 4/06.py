# 6. Programe una aplicación de consola que pregunte el precio total de la cuenta, luego
# pregunte cuántos comensales hay. A continuación deberá dividir la cuenta total por el
# número de comensales y mostrar cuánto debe pagar cada persona.

def saldo_por_comensal():
    precio_de_la_cuenta = input ("Ingresa el precio de la cuenta.")
    cantidad_de_comensales = input ("Ingresa el número de comensales.")
    return print (float (precio_de_la_cuenta) / float (cantidad_de_comensales))

saldo_por_comensal()