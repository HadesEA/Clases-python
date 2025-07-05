alumno = {
    "nombre": "Juan",
    "edad": 20,
    "materias": ["matemáticas", "historias", "química"]
}

print(alumno)
# Agregar un nuevo elemento a la lista de materias
alumno["materias"].append("física")
alumno["edad"] = 21
alumno["Contacto"] = {"teléfono": "123-456-7890", "email": "example@gmail.com"}

# Imprimir el objeto alumno con los cambios
for clave, valor in alumno.items():
    print(f"{clave}: {valor}")

for clave, valor in alumno.items():
    if isinstance(valor, dict):
        print(f"{clave}:")
        for subclave, subvalor in valor.items():
            print(f"  {subclave}: {subvalor}")
    else:
        print(f"{clave}: {valor}")
