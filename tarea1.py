
calificacion= float(input("ingresa por favor tu calificacion como número decimal: ", ))


if calificacion < 60:
    print("losiento, has suspendido.Debes esforzarte más en la proxima evaluación")
elif calificacion < 70: 
    print("Has aprobado, pero necesitas mejorar un poco.")
elif calificacion < 90:
    print("Has aprobado satisfactoriamente" )
else:
    print("¡felicitaciones! Has aprobado con una calificación sobresaliente.")

