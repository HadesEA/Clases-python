############################## LISTAS ###############################
frutas = ["manzana", "banana", "cereza", "frambuesa", "limon"]

print(frutas[0])         # manzana
frutas.append("kiwi")   # añade al final
print(frutas)
frutas.insert(1, "pepino") # Inserta un valor en una posición especificada
print(frutas)
frutas.remove("kiwi") # Elimina el valor de la lista que concuerde con el nombre brindado
print(frutas)
ultimo = frutas.pop() # Elimina y devuelve el último elemento de la lista
print(ultimo)
print(frutas)
ultimo1 = frutas.pop(1) # Elimina y devuelve el valor seleccionado de la lista
print(ultimo1)
print(frutas)
frutas.extend(["mango", "melon"])
print(frutas)

frutas[1] = "pera"      # cambia valor
print(frutas)
frutas.reverse() # invierte el orden de la lista, modificandola 
print(frutas)

print(len(frutas))      # longitud [4]

# aquí se imprime la longitud de cada fruta dentro de la lista frutas
# Usando List Comprehension
longitudes = [len(fruta) for fruta in frutas]
print(longitudes)   


numeros = [5, 3, 6, 2, 7, 1]
numeros.sort() # Sort nos permite ordenar la lista de manera automática
print(numeros)
numeros.sort(reverse=True) # También podemos orderar inversamente la lista de esta manera
print(numeros)

original = [8, 7, 6, 5, 3, 1, 2, 2]
ordenada = sorted(original) # SORTED nos permite crear una nueva lista que almacene la lista ordenada, sin modificar ni afectar la lista original
print(original) # [8, 7, 6, 5, 3, 1]
print(ordenada) # [1, 3, 5, 6, 7, 8]

print(original.count(2)) # Nos devuelve la cantidad de veces que aparece el número que le pedimos.
print(original.index(2)) # Nos devuelve la posición del número que le pedimos, si el número se repido devuelve la posición del primero en aparecer.
print(frutas.index("manzana")) # Devuelve la posición del valor que le pedimos.



copia = frutas # Forma no recomendada de copiar los valores de una lista
# Forma recomendadas de copiar una lista
copia = frutas.copy()
copia = frutas[:] 
copia = list(frutas)



############################## TUPLAS ###############################
# Las tuplas son iguales que las listas pero no puedes modificar su valor
punto = (10, 20)

# esto no se puede, sale un error: 
# punto[0] = 5

print(punto[0])    # 10

# De esta manera asignamos los valores de la tupla a las variables:
x, y = punto
print(f"x={x}, y={y}")

############################## DICCIONARIOS ###############################
# Los diccionarios son como listas pero con clave y valor
# Los diccionarios son mutables
persona = {"nombre": "Juan", "edad": 30}

print(persona["nombre"])
persona["ciudad"] = "Tijuana"
print(persona)

for clave, valor in persona.items():
    print(f"{clave}: {valor}")

############################## CONJUNTOS ###############################
# No ordenados y no permiten duplas
# Los conjuntos son mutables 
conjunto = {1, 3, 2, 2, 1}
print(conjunto)
