try:
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    opcion = int(input("Qué operación desea realizar? "))
except ValueError:
    print("Debes ingresar un número válido")
else:
    if opcion == 1:
        print(f"La suma de ambos números es: {num1 + num2}")
    elif opcion == 2:
        print(f"La resta de los números dados es: {num1 - num2}")
    elif opcion == 3:
        print(f"La multiplicación de ambos números es: {num1 * num2}")
    elif opcion == 4:
        try:
            print(f"La división resultante es: {num1 / num2}")
        except ZeroDivisionError:
            print("Error: No se puede dividir por cero")
    else: 
        print("Opción no válida")
finally:
    print("Fin del programa")