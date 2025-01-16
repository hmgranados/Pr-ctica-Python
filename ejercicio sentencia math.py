#ingresar un numero y decir si es par o impar

numero=int(input("ingresa un numero entero: ", ))

match numero:
    case 0:
      print("el número es un cero")
    case numero if numero % 2 == 0: #si el residuo es 0 es par
      print("el número", numero, "es par")
    case numero if numero % 2 != 0:
       print("el número", numero, "no es par ")
    case _:
      print("número no reconocido, por favor ingrese otro número")

    

