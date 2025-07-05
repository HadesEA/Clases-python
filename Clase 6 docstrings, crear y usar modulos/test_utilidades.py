from utilidades import saludar
import utilidades

print(saludar.__doc__) # Esta es la manera en la que se ve la documentación de una función importada
print(saludar("Juanito")) # Aquí usamos directamente la función ya que la importamos de manera directa desde utilidades con {from utilidades import saludar}

print(utilidades.cuadrado.__doc__) # Esta también es la manera en la que se ve la documentación de una función importada
print(utilidades.cuadrado(10)) # Aquí usamos la función cuadrado como un atributo del objeto utilidades