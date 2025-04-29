numero=[1,2,3,4,5]

numero_agregar=int(input("Que numero quieres agregar"))
posicion=int (input("en que posicion quieres agregar el digito(0,4)"))

numero_agregar=numero.insert(posicion,numero)

print("lista actualizada", numero)