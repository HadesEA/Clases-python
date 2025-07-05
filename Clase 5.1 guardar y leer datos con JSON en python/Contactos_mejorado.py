import json

# Intentamos cargar el archivo JSON
try:
    with open("contactos.json", "r") as archivo:
        contactos = json.load(archivo)
except FileNotFoundError:
    contactos = {}

opcion = 0
while opcion != 5:
    print("\n\nMENÚ DE CONTACTOS")
    print("1. Añadir contacto")
    print("2. Mostrar contactos")
    print("3. Modificar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")
    opcion = int(input("Ingrese la opción: "))

    if opcion == 1:
        nombre = input("Ingrese el nombre del contacto: ").strip().title()
        telefono = input("Ingrese el teléfono del contacto: ")
        email = input("Ingrese el correo electrónico del contacto: ")
        contactos[nombre] = {"telefono": telefono, "email": email}
        print(f"Contacto '{nombre}' añadido correctamente.")
    elif opcion == 2:
        print("\n--- Lista de contactos ---")
        if contactos:
            for clave, valor in contactos.items():
                print(f"{clave}")
                for subclave, subvalor in valor.items():
                    print(f"  {subclave}: {subvalor}")
        else:
            print("No hay contactos registrados.")
    elif opcion == 3:
        print("Contactos disponibles:", ", ".join(contactos.keys()))
        nombre = input("Ingrese el nombre del contacto a modificar: ").strip().title()
        if nombre in contactos:
            telefono = input("Nuevo teléfono: ")
            email = input("Nuevo correo electrónico: ")
            contactos[nombre]["telefono"] = telefono
            contactos[nombre]["email"] = email
            print(f"Los datos de {nombre} han sido actualizados.")
        else:
            print("El contacto no existe.")
    elif opcion == 4:
        print("Contactos disponibles:", ", ".join(contactos.keys()))
        nombre = input("Ingrese el nombre del contacto a eliminar: ").strip().title()
        if nombre in contactos:
            contactos.pop(nombre)
            print(f"El contacto '{nombre}' ha sido eliminado.")
        else:
            print("El contacto no existe.")
    elif opcion == 5:
        print("Hasta luego, vuelve pronto!")
    else:
        print(f"Seleccionaste una opción no válida: {opcion}")

    # Guardar contactos actualizados en el archivo JSON
    with open("contactos.json", "w") as archivo:
        json.dump(contactos, archivo, indent=4)
