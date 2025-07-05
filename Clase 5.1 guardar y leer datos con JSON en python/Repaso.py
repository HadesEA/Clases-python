# Los archivos JSON son (JavaScript Object Notation) archivos ligeros y legibles que 
# almacenan datos en formato JS, pudiendo ser diccionarios, listas, números y cadenas
# Python cuenta con un módulo llamado JSON del cuál se puede usar:

# import json Es necesario para poder utilizar este módulo

# Estos dos son utilizados para convertir datos de Python a JSON 
# json.dump()
# json.dumps()


# Estos son utilizados para convertir JSON a datos Python
# json.load()
# json.loads()

import json

contactos = {}

# with open("contactos.json", "w") as archivo: # La {w} es para que se escriba en el archivo (sobreescribiendo)
#     json.dump(contactos, archivo, indent=4)

with open("contactos.json", "r") as archivo: # La (r) es para que se lea el archivo
    contactos = json.load(archivo)

print(contactos)
