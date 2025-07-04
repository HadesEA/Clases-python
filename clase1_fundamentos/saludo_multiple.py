def saludar_personas(*nombres, saludar="Hola, buenas tardes"):
    for nombre in nombres:
        print(f"{saludar} {nombre}")

saludar_personas("Juan", "Pedro", "Ana")

# Guardar los saludos en una lista y retornar la lista en lugar de los saludos
def saludar_personas(*nombres, saludar="Aloooooh"):
    saludos = []
    for nombre in nombres:
        saludos.append(f"{saludar} {nombre}")
    return saludos

saludos = saludar_personas("Juan", "Pedro", "Ana")
print(saludos)  # ['Aloooooh Juan', 'Aloooooh Pedro'. 'Aloooooh Ana']

# Versión compacta devolviendo la lista utilizando list commprehension
def saludar_personas(*nombres, saludar="Hola, buenas tardes"):
    return [f"{saludar} {nombre}" for nombre in nombres] 

lista_saludos = saludar_personas("Juan", "Pedro", "Ana", saludar="¡Qué tal!")

for saludo in lista_saludos:
    print(saludo)
