#Escribe un programa Python que solicite al usuario 
# ingresar un número entero y luego determine en qué 
# rango se encuentra ese número utilizando la declaración match.
#  El programa debe imprimir un mensaje que indique el rango al
#  que pertenece el número.

numero= int(input("ingresa por favor un numero entero:", ))

match numero:

    case numero if numero < 0:
        print("El número ", numero," es negativo ")
    case numero if numero >= 0 and numero <10 :
        print("El número ", numero, "esta entre 0 y 10")
    case numero if numero >=10:
        print("El número ", numero, "es mayor o igual a 10")
    case _:
        print(f"El número {numero} no se encuentra en ningún rango conocido.")
        



