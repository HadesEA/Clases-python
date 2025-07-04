#Crea un script llamado mi_perfil.py que:
# Pida al usuario:
# Su nombre
# Su edad
# Calcule en qué año tendrá 100 años.
from datetime import datetime
name = input("¿Cómo te llamas? :) ")
try:
    edad = int(input("¿Cuántos años tienes? :) "))
except ValueError:
    print("Debes ingresar un número")
    exit()

# Calcula en qué año tendrá 100 años
año = datetime.now().year
año_nacimiento = año - edad
año_100 = año_nacimiento + 100
print(f"Hola {name}, tienes {edad} y en el año {año_100} tendrás 100 años")