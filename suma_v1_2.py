class OperacionAritmeticas:

    def ingresoNumeros(self):
        numero01 = int(input("Ingrese primer número: "))
        numero02 = int(input("Ingrese segundo número: "))
        return numero01, numero02

    def suma(self, numero01, numero02):
        return numero01 + numero02


