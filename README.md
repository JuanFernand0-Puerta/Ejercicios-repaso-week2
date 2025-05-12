# Ejercicios-repaso-week2

# Códigos ANSI para colorear mensajes en la consola
warning = "\033[93m"
danger = "\033[91m"
success = "\033[92m"
reset = "\033[0m"

# Diccionario vacío para agregar productos
inventary = {}

# Función para agregar un producto al inventario
def add_product(inventary, name_product, price, amount):
    if name_product in inventary:
        inventary[name_product]["cantidad"] += amount
        inventary[name_product]["precio"] = price
    else:
        inventary[name_product] = {"precio": price, "cantidad": amount}
    print(success + f"✅ Producto '{name_product}' agregado correctamente." + reset)

# Función para actualizar el precio
def update_price(inventary, name_product, new_price):
    inventary[name_product]["precio"] = new_price

# Función para buscar un producto
def search_product(inventary, name_product):
    if name_product in inventary:
        info = inventary[name_product]
        print(success + f"✅ {name_product}: Precio ${info['precio']}, Cantidad {info['cantidad']}" + reset)
    else:
        print(danger + "❌ Producto no encontrado." + reset)

# Función para eliminar un producto
def delete_product(inventary, name_product):
    if name_product in inventary:
        del inventary[name_product]
        print(success + f"✅ Producto '{name_product}' eliminado." + reset)
    else:
        print(danger + "❌ Producto no encontrado." + reset)

# Función para calcular el valor total del inventario
def calculate_total(inventary):
    total = sum(prod["precio"] * prod["cantidad"] for prod in inventary.values())
    return total

# Bucle principal
while True:
    print("\n=============================")
    print("    ¿Qué deseas hacer hoy?   ")
    print("=============================")
    print("1.) Añadir productos (mínimo 5 productos distintos)")
    print("2.) Consultar productos")
    print("3.) Actualizar precio de un producto")
    print("4.) Eliminar producto del inventario")
    print("5.) Calcular el valor total del inventario")
    print("6.) Salir del programa")

    choose_menu = input("Escoge una opción (1-6): ")

    if not choose_menu.isdigit() or not 1 <= int(choose_menu) <= 6:
        print(warning + "⚠ Opción inválida, intenta de nuevo." + reset)
        continue

    choose_menu = int(choose_menu)

    match choose_menu:
        case 1:
            temp_inventory = {}  # temporal para verificar cantidad mínima

            print(warning + "\n* Debes ingresar al menos 5 productos distintos." + reset)
            while len(temp_inventory) < 5:
                name_product = input("Nombre del producto: ").strip()
                if not name_product.isalpha():
                    print(danger + "❌ Nombre inválido." + reset)
                    continue

                try:
                    price = float(input("Precio del producto: "))
                    if price <= 0:
                        print(danger + "❌ El precio debe ser mayor que 0." + reset)
                        continue
                except:
                    print(danger + "❌ Precio inválido." + reset)
                    continue

                try:
                    amount = int(input("Cantidad del producto: "))
                    if amount <= 0:
                        print(danger + "❌ La cantidad debe ser mayor que 0." + reset)
                        continue
                except:
                    print(danger + "❌ Cantidad inválida." + reset)
                    continue

                # Guarda en temporal y en el inventario real
                temp_inventory[name_product] = True
                add_product(inventary, name_product, price, amount)

            print(success + f"\n✅ Se agregaron al menos {len(temp_inventory)} productos correctamente." + reset)

        case 2:
            name = input("Nombre del producto a buscar: ")
            search_product(inventary, name)

        case 3:
            name = input("Producto al que desea cambiar el precio: ")
            if name in inventary:
                try:
                    new_price = float(input("Nuevo precio: "))
                    if new_price > 0:
                        update_price(inventary, name, new_price)
                        print(success + f"✅ Precio actualizado." + reset)
                    else:
                        print(danger + "❌ El precio debe ser mayor que 0." + reset)
                except:
                    print(danger + "❌ Entrada inválida." + reset)
            else:
                print(danger + "❌ Producto no encontrado." + reset)

        case 4:
            name = input("Producto a eliminar: ")
            delete_product(inventary, name)

        case 5:
            total = calculate_total(inventary)
            print(success + f"💰 Valor total del inventario: ${total:.2f}" + reset)

        case 6:
            print(success + "¡Gracias por usar el programa!" + reset)
            break
            
