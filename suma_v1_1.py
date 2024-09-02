def ingresoNumeros():
    numero01 = int(input("Ingrese primer numero: "))
    numero02 = int(input("Ingrese segundo numero; "))
    return numero01, numero02
def suma(numero01,numero02):
    return numero01 + numero02

if __name__ == '__main__':
    num1, num2 = ingresoNumeros()
    print(f"{numero01} + {numero02} = {suma(num1, num2)}")