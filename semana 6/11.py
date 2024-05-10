#   PARTE 2 - ESTRUCTURAS DE CONTROL
#   Que solicite al usuario ingresar una frase. Luego, que imprima la cantidad de vocales que se
#   encuentran en dicha frase.

def cantidad_de_vocales():
    frase=""
    while frase =="":
        
        contador=0
        frase=input("Ingresa una frase para saber cuantas vocales posee: ").lower()
    #   validamos que la frase exista

    for caracter in frase:
        match caracter:
            case "a":
                contador+=1
            case "e":
                contador+=1
            case "i":
                contador+=1
            case "o":
                contador+=1
            case "u":
                contador+=1
    #   contamos para cada vocal
    return print(contador)

cantidad_de_vocales()