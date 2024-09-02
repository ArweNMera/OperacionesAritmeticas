def ingresoNumeros():
    numero01 = int(input("Ingrese primer número: "))
    numero02 = int(input("Ingrese segundo número: "))
    return numero01, numero02

def suma(numero01, numero02):
    return numero01 + numero02

if __name__ == '__main__':
    num1, num2 = ingresoNumeros()
    print(f"{num1} + {num2} = {suma(num1, num2)}")
