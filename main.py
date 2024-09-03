
from operacionesBas import CalculadoraMCD

if __name__ == "__main__":
    # Ejemplo de uso
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))

    calculadora = CalculadoraMCD(numero1, numero2)
    mcd = calculadora.calcular_mcd()
    mcm = calculadora.calcular_mcm()

    print(f"El MCD de {numero1} y {numero2} es {mcd}")
    print(f"El MCM de {numero1} y {numero2} es {mcm}")