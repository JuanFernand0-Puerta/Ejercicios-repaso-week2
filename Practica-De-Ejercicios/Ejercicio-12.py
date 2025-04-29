frutas=["mango","fresa","limon"]


print("Lista de frutas",frutas)
escoger= input("Que fruta quieres eliminar, selecciona una de la lista")

if escoger in frutas:
    frutas.remove(escoger)
    print ("fruta eliminada.")
else:
    print("la fruta no esta en la lista")
print("lista actualizada",frutas)