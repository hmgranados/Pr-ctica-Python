
calificacion= float(input("ingresa por favor tu calificacion como número decimal: ", ))


if (calificacion % 1 ) == 0 :
    print("el numero ingresado no es válido, por favor ingresa tu calificacion como número decimal ",   )
elif calificacion <= 4.9:
    print("No pasaste tu rendimiento no fue bueno, debes mejorar")
elif calificacion <= 6.9: 
    print("lograste pasar, ¡estas aprobado!")
elif calificacion <= 8.9:
    print("lo hiciste muy bien, tu rendimeinto fue notable! :" )
else:
    print("¡felicitaciones! tu rendimiento fue sobresaliente")
          

