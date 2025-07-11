""" Manera de utilizar un archivo de otra carpeta (carpeta que contiene espacios en el nombre) 
El código comentado abajo debe ir en el archivo en el que vamos a usar esta librería de manera importada
"""
# import os
# import sys

# ruta_absoluta = os.path.abspath("Clase 6 docstrings, crear y usar modulos")
# sys.path.append(ruta_absoluta)
# print(ruta_absoluta)
# print(os.listdir(ruta_absoluta))
# import calculadora

class calculadora: # Se recomienda usar la primera letra en mayúscula para que sea más identificable.
    def __init__(self, x, y): # Constructor de la clase Calculadora
        self.x = x
        self.y = y
    
    def sumar(self):
        """
        Se recibe el objeto self del cuál se toman los valores x y y 
        los cuales contienen los números brindados por el usuario

        Dentro de la función se utilizan ambos números para sumarlos y devolver el resultado
        """
        return self.x + self.y
    
    def restar(self):
        """
        Se recibe el objeto self del cuál se toman los valores x y y 
        los cuales contienen los números brindados por el usuario

        Dentro de la función se utilizan ambos números para restarlos y devolver el resultado
        """
        return self.x - self.y
    
    def multiplicar(self):
        """
        Se recibe el objeto self del cuál se toman los valores x y y 
        los cuales contienen los números brindados por el usuario

        Dentro de la función se utilizan ambos números para multiplicarlos y devolver el resultado
        """        
        return self.x * self.y
    
    def dividir(self):
        """
        Se recibe el objeto self del cuál se toman los valores x y y 
        los cuales contienen los números brindados por el usuario

        Dentro de la función se utilizan ambos números para dividirlos y devolver el resultado
        """        
        return self.x / self.y
    
    def potencia(self):
        """
        Se recibe el objeto self del cuál se toman los valores x y y 
        los cuales contienen los números brindados por el usuario

        Dentro de la función se utilizan ambos números tomando y como la potencia a la que se elevará x
        """        
        return self.x ** self.y
    
    def raiz(self):
        """
        Se recibe el objeto self del cuál se toma el valor de x 
        el cuál contiene el número brindado por el usuario

        Dentro de la función se saca la raiz cuadrada del número x
        """        
        return self.x ** 0.5