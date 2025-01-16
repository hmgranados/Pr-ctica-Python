#misma comparativa de if
#solo se ejecuta el primer caso que sea verdadero 
numero=4 #dado que el valor almacenado en número es 3

match numero:
    case 1:
        print("uno")
    case 2:
        print("dos")
    case 3:
        print("tres") #se imprime esto 
    case _:
        print("Número no encontrado")
