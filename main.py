
from operacionesAritmeticas import OperacionAritmeticas

if __name__ == '__main__':
    operacion = OperacionAritmeticas()
    num1, num2 = operacion.ingresoNumeros()  # Llamada correcta al método
    print(f"{num1} + {num2} = {operacion.suma(num1, num2)}")

