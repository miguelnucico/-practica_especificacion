from Clases.ejemplo.calculadora import Calculadora


class Menu(object):
    def __init__(self):
        self.opcion = 0

    def mostrarMenu(self):
        print("")
        print("Ejemplo programacion aplicada")
        print("1. Calculadora")
        print("0. Salir")

    def menu(self):
        self.opcion = ""
        while self.opcion != "0":
            self.mostrarMenu()
            self.opcion = input("Ingrese una opción: ")
            if self.opcion == "1":
                casio = Calculadora()
                casio.leerNumeros()
                casio.calcularSuma()
                casio.mostrarSuma()
              
            else:
                print("Opción inválida. Intente nuevamente.")
