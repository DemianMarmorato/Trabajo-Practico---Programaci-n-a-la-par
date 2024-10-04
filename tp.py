# TP Programación a la Par.
# Integrantes: Brito Thiago Ignacio y Marmorato Demian Alexander.
# División 115.


inventario = [
    {"nombre": "Chupetin Sable de luz", "cantidad": 50, "precio": 200},
    {"nombre": "Agua La Fuerza", "cantidad": 35, "precio": 3200},
    {"nombre": "Gomitas Holocubo", "cantidad": 25, "precio": 990},
    {"nombre": "Barrita de Cereal Wookiee", "cantidad": 48, "precio": 2500},
    {"nombre": "Galletitas R2D2", "cantidad": 20, "precio": 15800},
]

def agregar_producto(inventario, nombre, cantidad, precio):
    """
    Agrega un producto al inventario.

    Args:
        inventario (list): Lista de productos en el inventario.
        nombre (str): El nombre del producto a agregar.
        cantidad (int): La cantidad disponible del producto.
        precio (float): El precio unitario del producto.
    """
    producto = {
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio
    }
    inventario.append(producto)
    print(f"Producto '{nombre}' agregado exitosamente al inventario.")


def realizar_venta(inventario):
    """
    Realiza la venta de un producto, restando la cantidad comprada del inventario.
    El usuario deberá ingresar el nombre correcto de un producto antes de continuar.

    Args:
        inventario (list): Lista de productos en el inventario.
    """
    if len(inventario) == 0:
        print("No hay productos disponibles para la venta.")
        return

    mostrar_productos(inventario)
    producto_seleccionado = None
    while not producto_seleccionado:
        nombre_producto = input("Ingrese el nombre del producto que desea comprar: ")
        # Buscar si el producto existe en el inventario
        for producto in inventario:
            if producto["nombre"].lower() == nombre_producto.lower():
                producto_seleccionado = producto
                break
        if not producto_seleccionado:
            print(f"El producto '{nombre_producto}' no está en el inventario. Intente nuevamente.")

    cantidad_comprar = int(input(f"Ingrese la cantidad de {producto_seleccionado['nombre']} que desea comprar: "))

    if cantidad_comprar <= producto_seleccionado["cantidad"]:
        total = cantidad_comprar * producto_seleccionado["precio"]
        producto_seleccionado["cantidad"] -= cantidad_comprar
        print(f"Venta realizada. Total a pagar: ${total:.2f}")
    else:
        print("No hay suficiente stock disponible para realizar la venta.")


def mostrar_productos(inventario):
    """
    Muestra todos los productos disponibles en el inventario.

    Args:
        inventario (list): Lista de productos en el inventario.
    """
    if len(inventario) == 0:
        print("No hay productos en el inventario.")
    else:
        print("Productos disponibles:")
        for producto in inventario:
            print(f"Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: ${producto['precio']:.2f}")


def menu_principal():
    """
    Función principal que muestra el menú y gestiona las opciones seleccionadas por el usuario.
    El usuario puede agregar productos, realizar ventas, mostrar productos disponibles o salir del sistema.

    Args:
        Ninguno
    """
    while True:
        print("\n--- Menú Principal ---")
        print("1. Agregar producto al inventario")
        print("2. Realizar una venta")
        print("3. Mostrar productos disponibles")
        print("4. Salir del sistema")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad disponible: "))
            precio = float(input("Ingrese el precio unitario: "))
            agregar_producto(inventario, nombre, cantidad, precio)

        elif opcion == "2":
            realizar_venta(inventario)

        elif opcion == "3":
            mostrar_productos(inventario)

        elif opcion == "4":
            print("Saliendo del sistema. ¡Gracias por usar Yoda's Snack!")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

menu_principal()
