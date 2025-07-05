# Declaraciones de variables
vacia = []
a = 0

# Lógica o cuerpo del programa

# Forma que conozco jsjs
# while a < 3:
#     vacia.append(input("Ingrese el nombre de una fruta "))
#     a += 1

# Método más actual
for _ in range(3):
    vacia.append(input("Ingrese el nombre de una fruta: "))

print(f"Lista: {vacia}")

# Ordenamos la lista
vacia.sort()
print(f"Lista ordenada: {vacia}")

# Agregamos la fruta kiwi en la posición 2 de la lista
vacia.insert(2, "kiwi")
print(f"Inserción de kiwi: {vacia}")

# Eliminamos la primera fruta
vacia.pop(0)
print(f"Eliminamos la primera fruta: {vacia}")

