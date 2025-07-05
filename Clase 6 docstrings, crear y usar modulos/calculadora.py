def sumar(a, b):
    """
    Función que suma dos números

    Parámetros:
    a (int o float): Primer número
    b (int o float): Segundo número

    Retorna:
    int o float: La suma de a y b
    """
    return a + b

def restar(a, b):
    """
    Función que resta dos números

    Parámetros:
    a (int o float): Primer número
    b (int o float): Segundo número

    Retorna:
    int o float: La resta de a y b
    """
    return a - b

def multiplicar(a, b):
    """
    Función que multiplica dos números

    Parámetros:
    a (int o float): Primer número
    b (int o float): Segundo número

    Retorna:
    int o float: La multiplicación de a y b
    """
    return a * b

def dividir(a, b):
    """
    Función que divide dos números

    Parámetros:
    a (int o float): Primer número
    b (int o float): Segundo número

    Retorna:
    int o float: La división de a y b
    """
    if b == 0:
        return "No se puede dividir por cero" 
    return a / b

def elevar(a, b):
    """
    Función que eleva un número a la potencia del segundo número

    Parámetros:
    a (int o float): Primer número
    b (int o float): Segundo número

    Retorna:
    int o float: El elevado de a por b-veces
    """
    return a ** b

def raiz(a, b):
    """
    Función que devuelve las raices cuadradas de dos números

    Parámetros:
    a (int o float): Primer número
    b (int o float): Segundo número

    Retorna:
    tuple: (raíz de a, raíz de b)
    """
    return a ** 0.5, b ** 0.5

