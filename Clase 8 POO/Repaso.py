class Persona:
    def __init__(self, nombre, edad): # Constructor de la clase persona
        """Constructur que recibe nombre y edad"""
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        """Método que imprime un mensaje de saludo"""
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")

# p1 se vuelve la variable que almacena al objeto Persona, 
# el cuál recibe los valores "Hades" como nombre y 22 como edad
p1 = Persona("Hades", 22) 
p1.saludar()  # Imprime: Hola, soy Hades y tengo 22 años 