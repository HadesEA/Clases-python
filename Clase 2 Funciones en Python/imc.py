def calcular_imc(peso, altura):
    imc = peso / altura ** 2
    return imc

def valor_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif imc >= 30:
        return "Obesidad"
    else:
        return "Los valores brindados no se encuentran dentro del rango"

peso = int(input("¿Cuánto pesa (kg)? "))
altura = int(input("¿Cuanto mide (cm)? "))
altura = altura / 100

imc = calcular_imc(peso, altura)

print(f"Su IMC es de {imc:.2f}, el cuál corresponde con un {valor_imc(imc)}")

