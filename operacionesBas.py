class CalculadoraMCD:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def calcular_mcd(self):
        """Calcula el MCD de dos números usando el algoritmo de Euclides con restas sucesivas."""
        a, b = self.numero1, self.numero2
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return a

    def calcular_mcm(self):
        """Calcula el MCM de dos números usando la relación entre MCD y MCM."""
        mcd = self.calcular_mcd()
        mcm = abs(self.numero1 * self.numero2) // mcd
        return mcm