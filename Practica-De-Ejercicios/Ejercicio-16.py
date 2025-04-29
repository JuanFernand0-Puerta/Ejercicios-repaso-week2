list_num=["1","2","5","9"]

numero= str (input("dime tu numero que buscas"))

if numero in list_num:
    posicion=list_num.index(numero)
    print(f"el {numero} se encuentra en la siguiente posicion {posicion}.")
else:
    print(f"el numero {numero} no esta en la lista. ")


