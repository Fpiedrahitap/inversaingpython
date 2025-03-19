helados = []  # Lista para almacenar los helados
contadorId = 1  # Contador para asignar IDs únicos

while True:
    print("\nGestión de Helados")
    print("1. Agregar un helado")
    print("2. Ver lista de helados")
    print("3. Modificar un helado")
    print("4. Eliminar un helado")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":  # Agregar un helado
        nombre = input("Ingrese el nombre del helado: ")
        descripcion = input("Ingrese la descripción del helado: ")
        precio = input("Ingrese el precio del helado: ")
        
        if precio.isdigit():
            precio = float(precio)
            helado = {"id": contadorId, "nombre": nombre, "descripcion": descripcion, "precio": precio}
            helados.append(helado)
            contadorId += 1
            print("Helado agregado correctamente.")
        else:
            print("Error: El precio debe ser un número.")
    
    elif opcion == "2":  # Ver lista de helados
        if len(helados) == 0:
            print("No hay helados registrados.")
        else:
            print("\nLista de Helados:")
            for helado in helados:
                print(f"ID: {helado['id']}, Nombre: {helado['nombre']}, Descripción: {helado['descripcion']}, Precio: ${helado['precio']}")
    
    elif opcion == "3":  # Modificar un helado
        id_modificar = input("Ingrese el ID del helado a modificar: ")
        
        if id_modificar.isdigit():
            id_modificar = int(id_modificar)
            encontrado = False
            for helado in helados:
                if helado["id"] == id_modificar:
                    print(f"Helado encontrado: {helado}")
                    nuevo_nombre = input("Ingrese el nuevo nombre (deje en blanco para no modificar): ")
                    nueva_descripcion = input("Ingrese la nueva descripción (deje en blanco para no modificar): ")
                    nuevo_precio = input("Ingrese el nuevo precio (deje en blanco para no modificar): ")
                    
                    if nuevo_nombre:
                        helado["nombre"] = nuevo_nombre
                    if nueva_descripcion:
                        helado["descripcion"] = nueva_descripcion
                    if nuevo_precio and nuevo_precio.isdigit():
                        helado["precio"] = float(nuevo_precio)
                    
                    print("Helado modificado correctamente.")
                    encontrado = True
                    break
            if not encontrado:
                print("Error: No se encontró un helado con ese ID.")
        else:
            print("Error: El ID debe ser un número.")
    
    elif opcion == "4":  # Eliminar un helado
        id_eliminar = input("Ingrese el ID del helado a eliminar: ")
        
        if id_eliminar.isdigit():
            id_eliminar = int(id_eliminar)
            helados = [helado for helado in helados if helado["id"] != id_eliminar]
            print("Helado eliminado correctamente.")
        else:
            print("Error: El ID debe ser un número.")
    
    elif opcion == "5":  # Salir
        print("Saliendo del programa...")
        break
    
    else:
        print("Opción no válida. Intente nuevamente.")