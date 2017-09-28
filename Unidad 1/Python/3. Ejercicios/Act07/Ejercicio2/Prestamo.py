class Prestamo (object):

    cuenta_prestamos = 0
    acumula_prestamos = 0
    acumula_intereses = 0

    def __init__(self, capital, tipointeres, años):
        self.capital = capital
        self.tipointeres = tipointeres
        self.años = años
        Prestamo.cuenta_prestamos += 1
        Prestamo.acumula_prestamos += self.capital
        Prestamo.acumula_intereses += self.calcularInteres()

    def calcularInteres(self):
        return self.capital * self.tipointeres * self.años / 100

    def mostrar(self):
        print("Total de préstamos: {}".format(self.cuenta_prestamos))
        print("Capital prestado: {}".format(self.acumula_prestamos))
        print("Total de intereses: {}".format(self.acumula_intereses))