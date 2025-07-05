import calculadora

print(calculadora.sumar.__doc__)
print(calculadora.sumar(17, 19))

print(calculadora.restar.__doc__)
print(calculadora.restar(21, 8))

print(calculadora.multiplicar.__doc__)
print(calculadora.multiplicar(5, 7))

print(calculadora.dividir.__doc__)
print(calculadora.dividir(10, 0))  

print(calculadora.elevar.__doc__)
print(calculadora.elevar(3, 4))

print(calculadora.raiz.__doc__)
print(calculadora.raiz(16, 81))