personas = {"nombre": "Pancho", "edad": 21, "ciudad": "Guanajuato"}

# Acceder y modificar
print(personas["nombre"])

personas["edad"] = 26 # le cambiamos el valor edad
personas["correo"] = "correo@gmail.com"
print(personas)


print(personas.keys())
print(personas.values())

print(personas.items())
# La utilidad que se le puede dar a .items() es la siguiente:
for clave, valor in personas.items():
    print(f"{clave}: {valor}")

print(personas.get("edad","No existe"))
print(personas.pop("ciudad"))
print(personas)
personas.update({"Estado": "sobrio", "dia": "de la semana"})
print(personas)
personas.clear()
print(personas)

# Diccionarios anidados
contacto = {
    "nombre": "Ana",
    "telefonos": ["555-1234", "555-5678"],
    "direccion": {
        "ciudad": "CDMX",
        "colonia": "Centro"
    }
}
# Acceso a un valor dentro de un diccionario anidado:
print(contacto["telefonos"][0])           # 555-1234
print(contacto["direccion"]["colonia"])   # Centro
print(contacto["direccion"]["ciudad"])   # CDMX

# Podemos ir creando el diccionario de manera dinámica
nuevo = {}
nuevo["nombre"] = "Luis"
nuevo["edad"] = 20
print(nuevo)

