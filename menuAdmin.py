import json
proveedores = list ()

def mostrar_bienvenida_admin():
    mensaje = "********* 🔓 Bienvenido al modo Administrador 🔓 *********\nTe mostramos todo lo que podés hacer desde la app de tu consorcio, sin moverte de donde estés. Selecciona tu opción:\n"
    mensaje += "[1] Gestion de Usuarios\n"
    mensaje += "[2] Administrar Proveedores\n"
    mensaje += "[3] Obtener Reportes\n"
    mensaje += "[6] Salir del sistema\n"
    return mensaje

def mostrar_submenu(opcion):
    submenus = {
        1: {
            "mensaje": "Has seleccionado la opción 1: Gestion de Usuarios.",
            "opciones": {
                1: "Listar Usuarios",
                2: "Crear Usuario",
                3: "Eliminar Usuario",
                0: "Volver al Menú Principal"
            }
        },
        2: {
            "mensaje": "Has seleccionado la opción 2: Datos de proveedores.",
            "opciones": {
                1: "Listar Proveedores",
                2: "Modificar Proveeedores",
                3: "Eliminar Proveedores",
                4: "Agregar Nuevo Proveedor",
                0: "Volver al Menú Principal"
            }
        },
        3: {
            "mensaje": "Has seleccionado la opción 3: Reportes.",
            "opciones": {
                1: "Ultimas expensas",
                2: "Listar reclamos",
                0: "Volver al Menú Principal"
            }
        },
        6: {
            "mensaje": "Muchas Gracias por usar nuestro sistema. Vuelva pronto!",
            "opciones": {
             
            }
        }
    }

    submenu_info = submenus.get(opcion)
    if submenu_info:
        submenu_mensaje = submenu_info["mensaje"]
        submenu_opciones = submenu_info["opciones"]
        submenu = f"{submenu_mensaje}\n"
        for key, value in submenu_opciones.items():
            submenu += f"[{key}] {value}\n"
        return submenu
    elif opcion == 0:
        return mostrar_bienvenida_admin()
    else:
        return "Opción inválida. Por favor, selecciona una opción válida."

# Ejemplo de uso
opcion = None
while opcion != 6:
    bienvenida = mostrar_bienvenida_admin()
    print(bienvenida)

    opcion = int(input("Selecciona una opción: "))
    submenu = mostrar_submenu(opcion)
    print(submenu)

    if opcion == 1:
        subopcion = None
        while subopcion != 0:
            subopcion = int(input("Selecciona una opción del submenú: "))
            if subopcion == 0:
                break
            #aca van cada una de las subopciones del submenu 1:
            if subopcion == 1:
                print("Crear codigo para listar usuarios y contraseñas")
                print("[0] Volver al Menú Principal")
            if subopcion == 2:
                print("Crear codigo para poder CREAR NUEVOS USUARIOS")
                print("[0] Volver al Menú Principal")
            if subopcion == 3:
                print("Crear codigo para ELIMINAR USUARIO")
                print("[0] Volver al Menú Principal")
    if opcion == 2:
        subopcion = None
        while subopcion != 0:
            subopcion = int(input("Selecciona una opción del submenú: "))
            if subopcion == 0:
                break
            #aca van cada una de las subopciones del submenu 2:
            if subopcion == 1:
                print ("los proveedores actuales son: ")
                archivoProveedores = open("proveedores.json", "r") #si se mueve el archivo a otro file, modificar la ruta
                proveedores = json.loads(archivoProveedores.read())
                for proveedor in proveedores:
                    print ("-"*30)
                    for clave, valor in proveedor.items():
                        print (f"{clave}: {valor}")
                archivoProveedores.close
                print("[0] Volver al Menú Principal")

            if subopcion == 2:
                print("Los proveedores actuales son:")
                with open("proveedores.json", "r") as archivoProveedores:
                    proveedores = json.load(archivoProveedores)
                    for proveedor in proveedores:
                        print("-" * 30)
                        for clave, valor in proveedor.items():
                            print(f"{clave}: {valor}")

                opcion_proveedor = int(input("Ingrese el ID del proveedor que desea modificar (0 para volver): "))

                if opcion_proveedor == 0:
                # Volver al menú principal
                    break

                if opcion_proveedor > 0 and opcion_proveedor <= len(proveedores):
                    proveedor_seleccionado = proveedores[opcion_proveedor - 1]

                    # Realizar las modificaciones necesarias en el proveedor seleccionado
                    nuevo_consorcio = input("Ingrese el nuevo consorcio del proveedor: ")
                    nuevo_servicio = input("Ingrese el nuevo servicio del proveedor: ")
                    nuevo_proveedor = input("Ingrese el nuevo proveedor del proveedor: ")
                    nuevo_telefono = input("Ingrese el nuevo teléfono del proveedor: ")
                    nuevo_info = input("Ingrese la nueva info del proveedor: ")
                    proveedor_seleccionado["consorcio"] = nuevo_consorcio
                    proveedor_seleccionado["servicio"] = nuevo_servicio
                    proveedor_seleccionado["proveedor"] = nuevo_proveedor
                    proveedor_seleccionado["telefono"] = nuevo_telefono

                    # Guardar los datos modificados en el archivo JSON
                    with open("proveedores.json", "w") as archivoProveedores:
                        json.dump(proveedores, archivoProveedores, indent=4)

                    print("Proveedor modificado exitosamente.")
                    archivoProveedores.close
                else:
                    print("Opción inválida.")

            if subopcion == 3:
                print("Los proveedores actuales son:")
                with open("proveedores.json", "r") as archivoProveedores:
                    proveedores = json.load(archivoProveedores)
                    for proveedor in proveedores:
                        print("-" * 30)
                        for clave, valor in proveedor.items():
                            print(f"{clave}: {valor}")

                opcion_proveedor = int(input("Ingrese el ID del proveedor que desea ELIMINAR (0 para volver): "))

                if opcion_proveedor == 0:
                # Volver al menú principal
                    break

                if opcion_proveedor > 0 and opcion_proveedor <= len(proveedores):
                    proveedor_eliminado = proveedores.pop(opcion_proveedor - 1)
                
                    # Guardar los datos actualizados en el archivo JSON
                    with open("proveedores.json", "w") as archivoProveedores:
                        json.dump(proveedores, archivoProveedores, indent=4)

                    print(f"Proveedor eliminado exitosamente.")
                    archivoProveedores.close
                else:
                    print("Opción inválida.")    
                    
                print("[0] Volver al Menú Principal")

            if subopcion == 4:
                with open("proveedores.json", "r") as archivoProveedores:
                    proveedores = json.load(archivoProveedores)
                print("A continuacion agregue los datos del nuevo proveedor:")

                nuevo_consorcio = input("Ingrese la direccion de consorcio: ")
                nuevo_servicio = input("Ingrese el servicio: ")
                nuevo_proveedor = input("Ingrese el nombre del nuevo proveedor: ")
                nuevo_telefono = input("Ingrese teléfono: ")
                nuevo_info = input("Ingrese la informacion util: ")
                
                 # Crear el diccionario del nuevo proveedor
                nuevo_proveedor = {
                    "id": (len(proveedores))+1,
                    "consorcio": nuevo_consorcio,
                    "servicio": nuevo_servicio,
                    "proveedor": nuevo_proveedor,
                    "telefono": nuevo_telefono,
                    "info": nuevo_info
                }

                # Abrir el archivo JSON en modo de lectura
                with open("proveedores.json", "r") as archivoProveedores:
                    proveedores = json.load(archivoProveedores)

                    # Agregar el nuevo proveedor a la lista de proveedores
                    proveedores.append(nuevo_proveedor)

                # Guardar los datos actualizados en el archivo JSON
                with open("proveedores.json", "w") as archivoProveedores:
                    json.dump(proveedores, archivoProveedores, indent=4)

                print(f"el siguiente proveedor fue agregado exitosamente:")
                print(f"Proveedor '{nuevo_proveedor}")
                print("[0] Volver al Menú Principal")
        

    if opcion == 3:
            subopcion = None
            while subopcion != 0:
                subopcion = int(input("Selecciona una opción del submenú: "))
                if subopcion == 0:
                    break
                #aca van cada una de las subopciones del submenu 3:
                if subopcion == 1:
                    print("crear codigo para listar expensas")
                    print("[0] Volver al Menú Principal")
                if subopcion == 2:
                    print("crear codigo para listar los reclamos que genera el usuario")
                    print("[0] Volver al Menú Principal")

