################### TRY Y EXCEPT ###################
# Sirve para atrapar errores y evitar que el programa se detenga
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("¡No se puede dividir por cero!")

# Sirve también para capturar tipos específicos de errores
try:
    numero = int(input("Dime un número: "))
    resultado = 10 / numero
except ValueError:
    print("¡No has introducido un número!")
except ZeroDivisionError:
    print("¡No se puede dividir por cero!")





################## Else y Finally nos ayudan con el flujo del código: ##################
try:
    numero = int(input("Dame un número distinto de 0: "))
    resultado = 10 / numero
except ZeroDivisionError:
    print("¡Error: división por cero!")
except ValueError:
    print("Error: debes escribir un número válido.")
else:
    print(f"El resultado es {resultado}") # Else se ejecuta solo sino hubo error detectado
finally:
    print("Fin de la operación.") # Finally siempre se ejecuta sin importar si hubo error o no



####################### CAPTURA EL OBJETO DE LA EXCEPCIÓN ########################
try:
    x = int("abc")
except ValueError as e:
    print(f"Error: {e}") # e es el objeto de la excepción, que almacena el mensaje exacto del error

# Almacenar el mensaje del error es perfecto para debugging, ya que de dejarlo solo "except: " podríamos perder de vista
# incluso un error del sistema