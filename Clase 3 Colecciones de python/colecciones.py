# Lista 
lista = [10, 20, 30, 40, 50]
print(lista)
x = 0
# Correcto pero hay otra forma más simple
# def sumar_lista(x):
#     for numero in lista:
#         x = x + numero
#     return x

def sumar_lista(numeros):
    return sum(numeros)

# Correcto pero hay una forma más simple con LIST COMPREHENSION
# def doble_lista():
#     a = 0
#     for numeros in lista:
#         lista[a] = numeros * 2
#         a += 1
#     return lista

def doble_lista(numeros):
    return [n * 2 for n in numeros]

print(sumar_lista(lista))
print(doble_lista(lista))


# Diccionario
Nombres = {"nombre": "Juanito", "edad": 25, "ciudad": "Tijuana"}
for clave, valor in Nombres.items():
    print(f"{clave}: {valor}")
