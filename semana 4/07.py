#7. Pida al usuario un número x de días y luego mostrar por pantalla cuántas horas, minutos y
# segundos son esos números de días.

def tiempo():
    numero_de_dias = input ("Ingresa otro número de días.")
    return print ("días:" + str(numero_de_dias) + " horas:" + str ( int(numero_de_dias) * 24) + " minutos:" + str ( int (numero_de_dias) * 1440) + " Segundos:" + str ( int (numero_de_dias) * 86400))
#   Si una hora tiene 3600Segundos, 3600x24hs=86400 Segundos/Día, 60x24=1440Minutos/Día y finalmente 24hs/día

tiempo()