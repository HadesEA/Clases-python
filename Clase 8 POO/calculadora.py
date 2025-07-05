import libreria
try:
    opcion = 0
    while opcion != 7:
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Elevar")
        print("6. Raíz")
        print("7. Salir")
        opcion = int(input("Ingrese el número de la opción que desea realizar: "))
        if opcion == 1:
            x = float(input("Ingrese el primer número: "))
            y = float(input("Ingrese el segundo número: "))
            objeto = libreria.calculadora(x, y)
            print(f"\nEl resultado es: {objeto.sumar()}\n")
        elif opcion == 2:
            x = float(input("Ingrese el primer número: "))
            y = float(input("Ingrese el segundo número: "))
            objeto = libreria.calculadora(x, y)
            print(f"\nEl resultado es: {objeto.restar()}\n")
        elif opcion == 3:
            x = float(input("Ingrese el primer número: "))
            y = float(input("Ingrese el segundo número: "))
            objeto = libreria.calculadora(x, y)
            print(f"\nEl resultado es: {objeto.multiplicar()}\n")
        elif opcion == 4:
            x = float(input("Ingrese el primer número: "))
            y = float(input("Ingrese el segundo número: "))
            objeto = libreria.calculadora(x, y)
            print(f"\nEl resultado es: {objeto.dividir()}\n")
        elif opcion == 5:
            x = float(input("Ingrese el primer número: "))
            y = float(input("Ingrese el segundo número: "))
            objeto = libreria.calculadora(x, y)
            print(f"\nEl resultado es: {objeto.potencia()}\n")
        elif opcion == 6:
            x = float(input("Ingrese el número: "))
            objeto = libreria.calculadora(x,0)
            print(f"\nEl resultado es: {objeto.raiz()}\n")
        elif opcion == 7:
            print("Gracias por utilizar la calculadora")
        else:
            print("Opción no válida, ingrese un número válido... ")
except ValueError:
    print("Error, ingrese un número...")
except ZeroDivisionError:
    print("Error, no se puede dividir entre cero...")
else:
    print("Calculadora cerrada...")
finally:
    print("Fin del programa...")