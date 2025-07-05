contactos = {}

opcion = 0
while opcion != 5:
    print("\n\nMENÚ DE CONTACTOS")
    print("1. Añadir contacto ")
    print("2. Mostrar contactos ")
    print("3. Modificar contacto")
    print("4. Eliminar contacto ")
    print("5. Salir")
    opcion = int(input("Ingrese la opción: "))

    if opcion == 1:
        nombre = input("ingrese el nombre del contacto: ").script().title()
        telefono = input("ingrese el telefono del contacto: ")
        email = input("Ingrese el correo electrónico del contacto: ")
        contactos[nombre] = {"telefono": telefono, "email": email}
    elif opcion == 2:
        print("\n\n\n\n\n\n")
        for clave, valor in contactos.items():
            if isinstance(valor, dict):
                print(f"{clave}")
                for subclave, subvalor in valor.items():
                    print(f"  {subclave}: {subvalor}")
            else:
                print(f"{clave}: {valor}")
    elif opcion == 3:
        print(contactos.keys())
        nombre = input("ingrese el nombre del contacto a modificar: ").script().title()
        if nombre in contactos:
            telefono = input("ingrese el nuevo telefono del contacto: ")
            email = input("Ingrese el nuevo correo electrónico del contacto: ")
            contactos[nombre]["telefono"] = telefono
            contactos[nombre]["email"] = email
            print(f"Los datos de {nombre} han sido actualizados")
        else:
            print("El contacto no existe")
    elif opcion == 4:
        print(contactos.keys())
        nombre = input("Ingrese el nombre del contacto a eliminar: ").script().title()
        if nombre in contactos:
            eliminado = contactos.pop(nombre)
            print(f"\nEl contacto {nombre} ha sido eliminado")
        else: 
            print("El contacto no existe")
    elif opcion == 5:
        print("\n\n\n\nHasta luego, vuelve pronto!")
    else:
        print(f"Seleccionaste una opción no válida... {opcion}")
    print("\n\n")