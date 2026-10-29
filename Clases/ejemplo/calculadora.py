class Calculadora(object):
    def __init__(self):
        self.numero1 = 0
        self.numero2 = 0
        self.suma = 0

    def leerNumeros(self):
        self.numero1 = int(input("Numero 1:"))
        self.numero2 = int(input("Numero 2:"))

    def calcularSuma(self):
        self.suma = self.numero1 + self.numero2

    def mostrarSuma(self):
        print(f"La suma es:{self.suma}")

