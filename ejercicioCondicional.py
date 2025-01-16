
edad= int(input("por favor,ingresa tu edad: ", ))

#para evitar que ingrede datos negativos o que no existen en edad 

if edad <0 :
    print("edad no valida, por favor ingrese una edad valida")
elif edad <12 : 
    print("eres un niño")
elif edad <18:
    print("eres un adolecente")
elif edad < 65:
    print("eres un adulto")
else: 
    print("eres un viejo")   